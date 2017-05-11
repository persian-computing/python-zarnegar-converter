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
import struct
import logging

import zar1_encoding
from zar_file import ZarFile, ZarFileTypeError, OUTPUT_NEW_LINE


"""
Read-only view on a Zarnegar File

Generates a list of 80-byte-wide lines from a Zarnegar text or binary file.
"""


_LINE_WIDTH = 80

_BINARY_MAGIC = b'\x03\xCA\xB1\xF2'

_BINARY_HEADER_FMT = (
    '<' + # Little-Endian
    'H' + # Total Lines Count
    'H' + # Total Text Length
    '10s' # Installation/User Data
)
_binary_header_struct = struct.Struct(_BINARY_HEADER_FMT)

_BINARY_LINE_INFO_FMT = (
    '<' + # Little-Endian
    'B' + # Line Text Start
    'H' + # Cumulative Text Length
    'B'   # Line Text Length
)
_binary_line_info_struct = struct.Struct(_BINARY_LINE_INFO_FMT)


class Zar1File(ZarFile):

    @staticmethod
    def get(in_file):
        try:
            return Zar1BinaryFile(in_file)
        except ZarFileTypeError:
            return Zar1TextFile(in_file)

    def _append_line(self, text):
        rest = b' ' * (_LINE_WIDTH - len(text))
        self._lines.append(text + rest)

    # == Zar1, Text ==

    def get_zar1_text_output(self):
        return b''.join([
            line.rstrip() + OUTPUT_NEW_LINE
            for line in self.get_zar1_text_lines()
        ])

    def get_zar1_text_lines(self):
        return self._lines

    # == Unicode, Legacy ==

    def get_unicode_legacy_lro_output(self):
        return ''.join([
            line.rstrip() + OUTPUT_NEW_LINE
            for line in self.get_unicode_legacy_lro_lines()
        ])

    def get_unicode_legacy_lro_lines(self):
        return [
            zar1_encoding.convert_zar1_line_to_unicode_legacy_lro(zar1_line, line_no)
            for line_no, zar1_line in enumerate(self._lines, start=1)
        ]

    # == Unicode, Semantic, Left-to-Right Override ==

    def get_unicode_lro_output(self):
        return ''.join([
            line.rstrip() + OUTPUT_NEW_LINE
            for line in self.get_unicode_lro_lines()
        ])

    def get_unicode_lro_lines(self):
        return [
            zar1_encoding.convert_zar1_line_to_unicode_lro(zar1_line, line_no)
            for line_no, zar1_line in enumerate(self._lines, start=1)
        ]

    # == Unicode, Semantic, Right-to-Left Override ==

    def get_unicode_rlo_output(self):
        return ''.join([
            line.rstrip() + OUTPUT_NEW_LINE
            for line in self.get_unicode_rlo_lines()
        ])

    def get_unicode_rlo_lines(self):
        return [
            zar1_encoding.convert_zar1_line_to_unicode_rlo(zar1_line, line_no)
            for line_no, zar1_line in enumerate(self._lines, start=1)
        ]


class Zar1TextFile(Zar1File):

    def __init__(self, in_file):
        self._file = in_file
        self._lines = []
        self._read()

    def _read(self):
        logging.info(b'Reading Zar1 Text file...')
        self._file.seek(0)
        for line in self._file.readlines():
            text = line.rstrip()  # Drop CRLF
            self._append_line(text)


class Zar1BinaryFile(Zar1File):

    def __init__(self, in_file):
        self._file = in_file
        self._verify_magic_number()
        self._lines = []
        self._read()

    def _verify_magic_number(self):
        self._file.seek(0)
        magic = self._file.read(len(_BINARY_MAGIC))
        if magic != _BINARY_MAGIC:
            raise ZarFileTypeError("Not a Zar1 Binary File")

    def _read(self):
        logging.info(b'Reading Zar1 Binary file...')
        self._file.seek(len(_BINARY_MAGIC))

        header = _binary_header_struct.unpack(
            self._file.read(_binary_header_struct.size),
        )
        lines_count = header[0]

        line_infos = []
        for line_idx in range(lines_count):
            read_bytes = self._file.read(_binary_line_info_struct.size)
            line_info = _binary_line_info_struct.unpack(read_bytes)
            line_infos.append(line_info)

        for line_info in line_infos:
            left_indent = line_info[0]
            text_len = line_info[2]
            text = b' ' * left_indent + self._file.read(text_len)
            self._append_line(text)
