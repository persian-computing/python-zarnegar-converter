#!/usr/bin/env python
# coding: utf-8

# Copyright (C) 2017  Behnam Esfahbod
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author(s): Behnam Esfahbod <behnam@zwnj.org>


import os.path
from setuptools import setup, find_packages


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    readme = f.read()

setup(
    name='zarnegar-converter',
    version='0.1.3',
    description='Converter for Zarnegar Encoding and File Format to Unicode Text Files',
    author='Behnam Esfahbod',
    author_email='behnam@zwnj.org',
    maintainer='Behnam Esfahbod',
    maintainer_email='behnam@zwnj.org',
    url='https://github.com/behnam/python-zarnegar-converter',
    long_description=readme,
    license="GNU General Public License, Version 3",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: Persian",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Text Editors",
    ],

    include_package_data=True,
    package_data={
        '': ['*.txt', '*.rst'],
    },
    packages=find_packages('src'),
    package_dir={
        '':'src',
    },
    scripts=[
        "src/zarnegar-converter.py",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
