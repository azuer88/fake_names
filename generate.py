#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

GENDER = 0          # 0=Both, 1=Female, 2=Male
FIRSTNAMES = 2      # number of first names to use


def load_data():
    FOLDER = "./data/"
    FILES = ['male', 'female', 'last']
    data = {}
    # counts = {}

    for f in FILES:
        target = os.path.join(FOLDER, f)
        with open(target, "rt") as g:
            lines = g.read().splitlines()
        data[f] = lines
        # counts[f] = len(lines)

    # return {'data': data, 'counts': counts}
    return data


def generate(data, count):

    names = []

    return names


def main():
    data = load_data()
    # print data
    print data['counts']

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
