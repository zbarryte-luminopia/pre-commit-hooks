from __future__ import print_function

import argparse
from os import path
import re
import subprocess


WARNING_MSG = '{0} is {1} which over the threshold of {2} and therefore must be LFSed'


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--maximum-binary-size', type=int, required=True,
                        help='threshold size in bytes over which binary files must be LFSed')
    parser.add_argument('filenames', nargs='*', help='filenames to check')
    args = parser.parse_args(argv)

    lfs_ls_files = subprocess.check_output(['git', 'lfs', 'ls-files']).split('\n')
    lfs_files = [l[13:] for l in lfs_ls_files if len(l) > 13]
    lfs_status = subprocess.check_output(['git', 'lfs', 'status']).split('\n')
    # TODO use non-porcelain command to get newly tracked + staged LFS files
    status_regex = re.compile('^\t(.+?) \(.+?\)$')
    for line in lfs_status:
        match = status_regex.match(line)
        if match:
            lfs_files.append(match.group(1))

    retcode = 0
    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            if '\0' not in inputfile.read(8000):
                continue # File doesn't appear to be binary
        if filename not in lfs_files:
            size = path.getsize(filename)
            if size > args.maximum_binary_size:
                print(WARNING_MSG.format(filename, sizeof_fmt(size),
                    sizeof_fmt(args.maximum_binary_size)))
                retcode = 1
    return retcode


if __name__ == '__main__':
    exit(main())
