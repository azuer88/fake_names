#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import sys
import os
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


def normalize_name(source_string):
    names = source_string.split()

    first = names.pop(0)
    if first[-1] == ",":
        # this is a last name
        last = first[:-1]
        names.append(last)
    else:
        names.insert(0, first)

    return names


def generate_username(lines, prefix=''):

    prepend = ''
    if 'PREFIX' in os.environ:
        prepend = os.environ['PREFIX']

    if prefix:
        prepend = prefix

    usernames = []
    for line in lines:
        names = normalize_name(line)

        for uname in make_username(names):
            if not user_exists(uname, usernames):
                break
        else:
            raise Exception("no suitable username found for %s" %
                            " ".join(names))

        usernames.append(uname)

        if prepend:
            yield "{}.{}\t{}".format(prepend.lower(), uname, line.strip())
        else:
            yield "{}\t{}".format(uname, line.strip())


def main():

    args = parse_args()
    prefix = args.prefix

    for username in generate_username(sys.stdin, prefix=prefix):
        print username

if __name__ == "__main__":
    sys.exit(main())
