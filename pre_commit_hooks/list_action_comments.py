from __future__ import print_function

import argparse
import os.path

ACTION_PATTERNS = [
    b'TODO',
    b'FIX'
]
WARNING_MSG = '[{0}:{1}] {2}'


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile):
                for pattern in ACTION_PATTERNS:
                    if pattern in line:
                        print(WARNING_MSG.format(
                            filename, i + 1, line.strip()
                        ))

    return 0


if __name__ == '__main__':
    exit(main())
