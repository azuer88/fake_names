#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import sys


def userline(line):
    words = line.split()
    username = words[0]
    fullname = " ".join(words[1:])
    return "{0}:password:::{1}:/home/{0}:/bin/bash".format(username, fullname)


def main():

    for line in sys.stdin:
        print userline(line)

if __name__ == "__main__":
    sys.exit(main())
