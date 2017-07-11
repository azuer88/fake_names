#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

import sys
import os
import argparse
import six

from genusername import generate_username
from userline import userline


def get_names(config):

    prefix = config["prefix"]
    source = config["source"]

    if isinstance(config['source'], six.string_types):
        with open(source, "r+t") as infile:
            for username in generate_username(infile, prefix):
                yield username
    else:
        for username in generate_username(source, prefix):
            yield username


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("source",
                        default="",
                        nargs="?",
                        help="Text file containing a user's full name per line")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--prefix", default="",
                       help="Prefix to prepend to generated username")
    group.add_argument("-n", dest="prepend",
                       action="store_true",
                       help="Do not get prefix from file name. " +
                       "Otherwise, prefix will be the first word in the " +
                       "filename components, as separated by a '.'")

    args = parser.parse_args()

    config = {}
    if args.source:
        config['source'] = args.source
        if not args.prepend:
            fname = os.path.basename(args.source)
            prefix = fname.split('.')[0]
        else:
            prefix = args.prefix
        config['prefix'] = prefix
    else:
        config['source'] = sys.stdin
        config['prefix'] = args.prefix

    # print args

    return config


def main():
    args = parse_args()
    # print args

    for name in get_names(args):
        print userline(name)


if __name__ == "__main__":
    sys.exit(main())
