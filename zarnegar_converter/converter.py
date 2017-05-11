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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
import os
import logging

from zar_file import ZarFile


"""
Converter for Zarnegar Encoding and File Format to Unicode Text
"""


_USAGE = '''\
Converter for Zarnegar Encoding and File Format to Unicode Text

Usage: %s <output-format> [<input-file> [<output-file> [<log-file>]]]

Arguments:
  output-format      desired output format (see list below)
  input-file         path to input file (default: stdin)
  output-file        path to output file (default: stdout)
  log-file           path to log file (default: stderr)

Output Formats:
  * unicode_rlo          Unicode Arabic semantic (standard) encoding, in Right-to-Left Override order
  * unicode_lro          Unicode Arabic semantic (standard) encoding, in Left-to-Right Override order
  * unicode_legacy_lro   Legacy Unicoe Arabic Presentation Form encoding, in Right-to-Left Override order
  * unicode_legacy_rlo   Legacy Unicoe Arabic Presentation Form encoding, in Left-to-Right Override order
  * zar1_text            Zar1 encoded (text file)
'''



def get_output_bytes(
    output_format,
    zar_file,
):
    # Zar1
    if output_format == 'zar1_text':
        return zar_file.get_zar1_text_output()

    # Unicode Legacy
    if output_format == 'unicode_legacy_lro':
        return zar_file.get_unicode_legacy_lro_output().encode('utf8')
    if output_format == 'unicode_legacy_rlo':
        return zar_file.get_unicode_legacy_rlo_output().encode('utf8')

    # Unicode Semantic
    if output_format == 'unicode_lro':
        return zar_file.get_unicode_lro_output().encode('utf8')
    if output_format == 'unicode_rlo':
        return zar_file.get_unicode_rlo_output().encode('utf8')

    raise UsageError("invalid output format: %s" % output_format)


def convert_and_write(
    output_format,
    in_file,
    out_file,
):
    zar_file = ZarFile.get(in_file)
    out_file.write(get_output_bytes(output_format, zar_file))


def main(
    output_format,
    in_filename=None,
    out_filename=None,
    log_filename=None,
):
    logging.basicConfig(level=logging.WARNING)
    if log_filename:
        logging.basicConfig(
            filename=log_filename,
            level=logging.DEBUG,
            filemode='w',
        )

    in_file = None
    out_file = None
    try:
        in_file = open(in_filename, 'r') if in_filename else sys.stdin
        out_file = open(out_filename, 'w') if out_filename else sys.stdout
        convert_and_write(output_format, in_file, out_file)
    except IOError:
        if not in_file:
            raise IOError("cannot read from input file: %s" % in_filename)
        if not out_file:
            raise IOError("cannot write to output file: %s" % out_filename)
    finally:
        if in_filename and in_file:
            in_file.close()
        if out_filename and out_file:
            out_file.close()


class UsageError (Exception):
    pass


def error(err_file, err):
    err_file.write("Error: %s%s" % (err, os.linesep))
    err_file.write(os.linesep)

def usage(err_file, script_name):
    err_file.write(_USAGE % script_name)

if __name__=='__main__':
    try:
        if len(sys.argv) < 2 or len(sys.argv) > 5:
            raise UsageError("invalid arguments")
        main(*sys.argv[1:])

    except UsageError as err:
        error(sys.stderr, err)
        usage(sys.stderr, os.path.basename(sys.argv[0]))
        exit(1)

    except IOError as err:
        error(sys.stderr, err)
        exit(2)
