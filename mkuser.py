#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import pwd
import fileinput


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


def process_names(line):
    names = line.split()


def main():
    usernames = []
    for line in fileinput.input():
        names = line.split()
        for uname in make_username(names):
            if not user_exists(uname, usernames):
                break
        usernames.append(uname)
        print "{}\t{}\n".format(uname, line)

if __name__ == "__main__":
    import sys
    sys.exit(main())
