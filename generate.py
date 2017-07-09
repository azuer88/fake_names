#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import re

from random import choice, sample

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


def generate_last_name(last):
    return choice(last)


def generate_first_name(first, first_count):
    # how many first name to generate
    if first_count > 1:
        fnc = choice(range(first_count)) + 1
    else:
        fnc = 1
    fnames = sample(first, fnc)
    first_name = " ".join(fnames)

    return first_name


def choose_first_names(data, gender):
    if gender == 0:
        return choice((data['male'], data['female']))
    elif gender == 1:  # Female
        return data['female']
    elif gender == 2:  # Male
        return data['male']
    else:
        raise Exception('Invalid gender value')


def generate(data, count):

    names = []

    for i in range(0, count):
        first_name = generate_first_name(
            choose_first_names(data, GENDER), FIRSTNAMES)
        last_name = generate_last_name(data['last'])

        names.append("%s %s" % (first_name, last_name))

    return names


def parse_args():
    parser = argparse.ArgumentParser(description="Generate random names")
    parser.add_argument('nspec',
                        type=str,
                        nargs='+',
                        help="a string specifying the type of " +
                        "name(s) to generate, (eg. 3F3 2m B")
    args = parser.parse_args()

    # print args.nspec
    specs = []
    rx = re.compile('(\d*)([FfMmBb])(\d*)')
    for arg in args.nspec:
        m = rx.match(arg)
        c, g, x = m.groups()
        if c is '':
            nc = 1
        else:
            nc = int(c)

        if x is '':
            nx = 1
        else:
            nx = int(x)

        gs = g.upper()
        if gs == 'B':
            gm = 0
        elif gs == 'F':
            gm = 1
        elif gs == 'M':
            gm = 2
        else:
            raise Exception("invalid gender type - %s" % m)

        specs.append((nc, gm, nx))
        return specs


def main():
    data = load_data()
    # print data
    # print data

    # for name in generate(data, 10):
    #     print name

    # print generate_first_name(choose_first_names(data, 0), 3)
    # print generate_last_name(data['last'])
    specs = parse_args()
    print specs
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
