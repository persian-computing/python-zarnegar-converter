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


OUTPUT_NEW_LINE = b'\r\n'


class ZarFile(object):

    @staticmethod
    def get(in_file):
        from zarnegar_converter.zar1_file import Zar1File
        return Zar1File.get(in_file)

    # == DEBUG ==

    def get_debug(self):
        raise NotImplementedError

    # == Zar1, Text ==

    def get_zar1_text_output(self):
        raise NotImplementedError

    def get_zar1_text_lines(self):
        raise NotImplementedError

    # == Unicode, Legacy ==

    def get_unicode_legacy_lro_output(self):
        raise NotImplementedError

    def get_unicode_legacy_lro_lines(self):
        raise NotImplementedError

    def get_unicode_legacy_rlo_output(self):
        raise NotImplementedError

    def get_unicode_legacy_rlo_lines(self):
        raise NotImplementedError

    # == Unicode, Semantic, Left-to-Right Override ==

    def get_unicode_lro_output(self):
        raise NotImplementedError

    def get_unicode_lro_lines(self):
        raise NotImplementedError

    # == Unicode, Semantic, Right-to-Left Override ==

    def get_unicode_rlo_output(self):
        raise NotImplementedError

    def get_unicode_rlo_lines(self):
        raise NotImplementedError


class ZarFileTypeError(Exception):
    pass
