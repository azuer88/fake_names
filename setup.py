#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

from setuptools import setup, find_packages

setup(
    name="pyhelpers",
    version="0.9a1",
    packages=find_packages(''),
    install_requires=['six', ],
    package_data={
        'data': ['/src/scripts/data/*', ],
    },

    # metadata
    author="Blue Cuenca",
    author_email="blue.cuenca@gmail.com",
    license="MIT",
    keywords="user batch creation",
    url="https://www.github.com/azuer88/pyhelpers",

    description="Helper python scripts for linux administration",
)
