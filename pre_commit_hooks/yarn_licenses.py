from __future__ import print_function

import argparse
from os import path
import json
import re
import subprocess

from tempfile import TemporaryFile


WARNING_MSG = '{0}@{1} has unapproved license "{2}"'


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--approved-licenses', type=lambda s: s.split(','), default=[],
                        help='comma delimited list of allowed SPDX licenses')
    parser.add_argument('--explicit-packages', type=lambda s: s.split(','), default=[],
                        help='comma delimited list of packages with explicitly approved licenses'
                        + 'and optional versions in the form PACKAGE_NAME::SPDX_LICENSE::VERSION?')
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)

    def process_explicit_package(item):
        info = item.split('::')
        version = info[2].strip() if len(info) == 3 else None
        return { 'package': info[0].strip(), 'license': info[1].strip(), 'version': version }
    explicit_packages = map(process_explicit_package, args.explicit_packages)

    retcode = 0
    for filename in args.filenames:
        if 'yarn.lock' in filename:
            # Load license information for this yarn.lock file into a temporary file, then read from it
            # This circumvents a limitation of subprocess which truncates the output of any line to 64k bytes
            with TemporaryFile() as stdout:
                subprocess.call(['yarn', 'licenses', 'ls', '--json'],
                               cwd=path.abspath(path.dirname(filename)),
                               stdout=stdout)
                stdout.seek(0)
                licenses_raw = stdout.read().split('\n')

            licenses_json = ''
            for line in licenses_raw:
                if '"type":"table"' in line:
                    licenses_json = json.loads(line)
                    break
            licenses = [dict(zip(licenses_json['data']['head'], d_arr)) for d_arr in licenses_json['data']['body']]
            # Check that all the licenses are valid
            for l in licenses:
                # TODO add support for ORed licenses
                # For now, it's possible to get around them by using an explicit package entry
                if l['License'] not in args.approved_licenses:
                    # Check if there is an explicit license for this package
                    exp = next((e for e in explicit_packages if e['package'] == l['Name']), None)
                    # TODO add explicit license wildcard support
                    if not exp or exp['license'] != l['License'] or (exp['version'] and exp['version'] != l['Version']):
                        print(WARNING_MSG.format(l['Name'], l['Version'], l['License']))
                        retcode = 1
            if retcode != 0:
                print('')
                print('Approved licenses: {}'.format(args.approved_licenses))
                print('Explicit packages:\n{}'.format(json.dumps(explicit_packages, indent=2)))
            return retcode


if __name__ == '__main__':
    exit(main())
