#!/usr/bin/env python
config = {
    "exes": {
        # Get around the https warnings
        "hg": ['/usr/local/bin/hg', "--config", "web.cacerts=/etc/pki/tls/certs/ca-bundle.crt"],
        "hgtool.py": ["/usr/local/bin/hgtool.py"],
        "gittool.py": ["/usr/local/bin/gittool.py"],
    },
    'gecko_pull_url': 'https://hg.mozilla.org/releases/b2g-ota',
    'gecko_push_url': 'ssh://hg.mozilla.org/releases/b2g-ota',
    'gecko_local_dir': 'b2g-ota',
    'git_ref_cache': '/builds/b2g_bumper/git_ref_cache.json',

    'manifests_repo': 'https://git.mozilla.org/b2g/b2g-manifest.git',
    'manifests_revision': 'origin/b2g-ota',

    'hg_user': 'B2G Bumper Bot <release+b2gbumper@mozilla.com>',
    "ssh_key": "~/.ssh/ffxbld_rsa",
    "ssh_user": "ffxbld",

    'hgtool_base_bundle_urls': ['https://ftp-ssl.mozilla.org/pub/mozilla.org/firefox/bundles'],

    'gaia_repo_url': 'https://hg.mozilla.org/integration/gaia-b2g-ota',
    'gaia_revision_file': 'b2g/config/gaia.json',
    'gaia_max_revisions': 1,
    # Which git branch this hg repo corresponds to
    'gaia_git_branch': 'b2g-ota',
    'gaia_git_repo': 'https://git.mozilla.org/releases/gaia.git',
    'gaia_mapper_project': 'gaia',
    'mapper_url': 'http://cruncher.build.mozilla.org/mapper/{project}/{vcs}/{rev}',

    'devices': {
        'emulator-kk': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        # Equivalent to emulator-ics - see bug 916134
        # Remove once the above bug resolved
        'emulator': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
            'manifest_file': 'emulator.xml',
        },
        'flame-kk': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
        },
        'aries': {
            'ignore_projects': ['gecko'],
            'ignore_groups': ['darwin'],
            'manifest_file': 'shinano.xml',
        },
    },
    'repo_remote_mappings': {
        'https://android.googlesource.com/': 'https://git.mozilla.org/external/aosp',
        'git://codeaurora.org/': 'https://git.mozilla.org/external/caf',
        'git://github.com/mozilla-b2g/': 'https://git.mozilla.org/b2g',
        'git://github.com/mozilla/': 'https://git.mozilla.org/b2g',
        'http://android.git.linaro.org/git-ro/': 'https://git.mozilla.org/external/linaro',
        'http://sprdsource.spreadtrum.com:8085/b2g/android': 'https://git.mozilla.org/external/sprd-aosp',
        'git://github.com/apitrace/': 'https://git.mozilla.org/external/apitrace',
        'git://github.com/t2m-foxfone/': 'https://git.mozilla.org/external/t2m-foxfone',
        # Some mappings to ourself, we want to leave these as-is!
        'https://git.mozilla.org/releases': 'https://git.mozilla.org/releases',
        'https://git.mozilla.org/integration': 'https://git.mozilla.org/integration',
        'https://git.mozilla.org/external/aosp': 'https://git.mozilla.org/external/aosp',
        'https://git.mozilla.org/external/caf': 'https://git.mozilla.org/external/caf',
        'https://git.mozilla.org/b2g': 'https://git.mozilla.org/b2g',
        'https://git.mozilla.org/external/apitrace': 'https://git.mozilla.org/external/apitrace',
        'https://git.mozilla.org/external/t2m-foxfone': 'https://git.mozilla.org/external/t2m-foxfone',
    },
}
