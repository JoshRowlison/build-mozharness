#!/usr/bin/env python

import sys
import os
import re

# load modules from parent dir
sys.path.insert(1, os.path.dirname(sys.path[0]))

# import the guts
from mozharness.base.script import BaseScript
from mozharness.base.python import VirtualenvMixin
from mozharness.base.script import ScriptMixin


class GetAPK(BaseScript, VirtualenvMixin, ScriptMixin):
    all_actions = [
        'create-virtualenv',
        'download-apk',
    ]

    config_options = [
        [["--build"], {
            "dest": "build",
            "help": "Specify build number (default 1)",
            "default": 1
        }],
        [["--version"], {
            "dest": "version",
            "help": "Specify version number to download (e.g. 23.0b7)"
        }],
        [["--arch"], {
            "dest": "arch",
            "help": "Specify which architecture to get the apk for",
            "default": "arm"
        }],
        [["--locale"], {
            "dest": "locale",
            "help": "Specify which locale to get the apk for",
            "default": "multi"
        }]
    ]

    arch_values = ("arm", "x86")

    def __init__(self, require_config_file=False, config={},
                 all_actions=all_actions):

        default_config = {
            # the path inside the work_dir ('build') of where we will install the env.
            # pretty sure it's the default and not needed.
            'virtualenv_path': 'venv',
        }

        default_config.update(config)

        BaseScript.__init__(
            self,
            config_options=self.config_options,
            require_config_file=require_config_file,
            config=default_config,
            all_actions=all_actions,
        )

    # Gets called once download is complete
    def download_complete(self, apk_file, checksum_file):
        self.info(apk_file + " has been download successfully")
        os.remove(checksum_file)

    def check_argument(self):
        """ Check that the given values are correct
        """

        if not isinstance(self.config['build'], int):
            self.fatal("Build number: " + self.config['build'] + " is not an integer")

        if self.config["version"] is None:
            self.fatal("Version is required")

        if self.config["arch"] not in self.arch_values:
            error = self.config["arch"] + " is not a valid arch.  " \
                                      "Try one of the following:"+os.linesep
            for arch in self.arch_values:
                error = error + arch + os.linesep
            self.fatal(error)

    def check_apk(self, apk_file, checksum_file):
        checksum = ScriptMixin.read_from_file(self, checksum_file, False)
        checksum = re.sub("\s(.*)", "", checksum.splitlines()[0])

        apk_checksum = self.file_sha512sum(apk_file)

        if checksum == apk_checksum:
            self.download_complete(apk_file, checksum_file)
        else:
            os.remove(apk_file)
            os.remove(checksum_file)
            self.fatal("Downloading " + apk_file + " failed!")

    def generate_url(self, version, arch, build, locale, android_layout, arch_file):
        return "https://ftp.mozilla.org/pub/mozilla.org/mobile/candidates/" + version + "-candidates/build" + build + \
               "/" + android_layout + "/" + locale + "/fennec-" + version + "." + locale + \
               ".android-" + arch_file

    def download(self, filename, url):
        apk_url = url + ".apk"
        checksum_url = url + ".checksums"
        filename_apk = filename + ".apk"
        ScriptMixin.download_file(self, apk_url, filename_apk)
        checksum_file = ScriptMixin.download_file(self, checksum_url, filename + ".checksums")
        self.check_apk(filename_apk, checksum_file)

    def download_apk(self):
        self.check_argument()
        version = self.config["version"]
        arch = self.config["arch"]
        build = str(self.config["build"])
        locale = self.config["locale"]

        if arch is "arm":
            android_layout = "v9_v11"
        else:
            android_layout = "android-"+arch

        if arch == "x86":
            # the filename contains i386 instead of x86
            arch_file = "i386"
        else:
            arch_file = arch

        self.info("Downloading version " + version + " build #" + build
                  + " for arch " + arch + " (locale " + locale + ")")

        if android_layout is "v9_v11":
            # When dealing with API v9 & V11, we want to rename the file
            # until bug 1122059 is fixed
            # Also manage the KO locale
            filename_arm_v9 = "fennec-" + version + "." + locale + ".android-arm-api-9"
            url = self.generate_url(version, arch, build, locale, "android-api-9", arch_file)
            self.download(filename_arm_v9, url)

            filename_arm_v11 = "fennec-" + version + "." + locale + ".android-arm-api-11"
            url = self.generate_url(version, arch, build, locale, "android-api-11", arch_file)
            self.download(filename_arm_v11, url)
        else:
            filename = "fennec-" + version + "." + locale + "." + "android-" + arch_file
            url = self.generate_url(version, arch, build, locale, android_layout, arch_file)
            self.download(filename, url)
# main {{{1
if __name__ == '__main__':
    myScript = GetAPK()
    myScript.run_and_exit()