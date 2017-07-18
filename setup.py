#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# author: Blue Cuenca <blue.cuenca@gmail.com>

from setuptools import setup, find_packages

setup(
    name="pyhelpers",
    version="0.9a2",
    packages=find_packages(),
    install_requires=['six', ],
    package_data={
        '': ['/pyhelpers/data/*', ],
    },
    include_package_data=True,
    # metadata
    author="Blue Cuenca",
    author_email="blue.cuenca@gmail.com",
    license="MIT",
    keywords="user batch creation",
    url="https://www.github.com/azuer88/pyhelpers",
    dependency_links=['https://github.com/azuer88/pyhelpers/tarball/master' +
                      '#egg=package-09a1', ],
    description="Helper python scripts for linux administration",
    classifiers=[
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utility',
    ],
    python_requires='>=2.7',
    entry_points={
        'console_scripts': [
                            'newusers-from=pyhelpers.mknewusersfrom:main',
                            'genusernames=pyhelpers.generate:main',
        ],
    },
)
