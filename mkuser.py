#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import sys
import pwd
import argparse


def make_username(names):

    initials = [x.lower()[0] for x in names[:-1]]
    surname = names[-1].lower()

    first = ''
    yield surname
    for i in initials:
        first = first + i
        yield "{}.{}".format(first, surname)

    for i in range(1, 10):
        yield "{}{}.{}".format(first, i, surname)


def user_exists(username, userlist, check_localdb=True):
    if username in userlist:
        return True
    if check_localdb:
        try:
            pwd.getpwnam(username)
            return True
        except KeyError:
            pass  # user does not exist
    return False


def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prefix",
                        default="",
                        help="prefix to prepend to usernames"
                        )

    args = parser.parse_args()

    return args


def main():

    args = parse_args()

    prefix = args.prefix

    usernames = []
    for line in sys.stdin:
        names = line.split()
        for uname in make_username(names):
            if not user_exists(uname, usernames):
                break
        usernames.append(uname)
        if prefix:
            print "{}.{}\t{}\n".format(prefix, uname, line)
        else:
            print "{}\t{}\n".format(uname, line)

if __name__ == "__main__":
    sys.exit(main())
