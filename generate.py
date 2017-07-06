#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
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


def main():
    data = load_data()
    # print data
    # print data

    for name in generate(data, 10):
        print name

    # print generate_first_name(choose_first_names(data, 0), 3)
    # print generate_last_name(data['last'])
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
