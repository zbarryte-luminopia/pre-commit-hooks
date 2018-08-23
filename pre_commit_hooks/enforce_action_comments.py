from __future__ import print_function

import argparse


WARNING_MSG = 'Actionable comment "{0}" found in {1}:{2}'


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--tags', type=lambda s: s.split(','), default=[],
                        help='comma delimited list of strings to look for, such as "FIXME"')
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'r') as inputfile:
            try:
                for i, line in enumerate(inputfile):
                    for pattern in args.tags:
                        if pattern in line:
                            print(WARNING_MSG.format(
                                pattern.decode(), filename, i + 1,
                            ))
                            retcode = 1
            except UnicodeDecodeError:
                continue

    return retcode


if __name__ == '__main__':
    exit(main())
