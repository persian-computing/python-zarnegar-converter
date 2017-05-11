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


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
    license = f.read()

setup(
    name='zarnegar-converter',
    version='0.1.0',
    description='Converter for Zarnegar Encoding and File Format to Unicode Text Files',
    long_description=readme,
    author='Behnam Esfahbod',
    author_email='behnam@zwnj.org',
    maintainer='Behnam Esfahbod',
    maintainer_email='behnam@zwnj.org',
    url='https://github.com/behnam/python-zarnegar-converter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: Persian",
        "Topic :: Software Development :: Internationalization",
        "Topic :: Text Editors",
    ],
    scripts=[
        "zarnegar_converter/converter.py",
    ],
)
