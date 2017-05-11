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


"""
Unicode Bidirection helpers for Zarnegar Encoding
"""


LRO = 0x202D # LEFT-TO-RIGHT OVERRIDE

LRO_CHAR = "\u202D"   # LEFT-TO-RIGHT OVERRIDE
RLO_CHAR = "\u202E"   # RIGHT-TO-LEFT OVERRIDE

MIRROR_MAP = {
    0x0028: 0x0029,   # LEFT PARENTHESIS
    0x0029: 0x0028,   # RIGHT PARENTHESIS

    0x003C: 0x003E,   # LESS-THAN SIGN
    0x003E: 0x003C,   # GREATER-THAN SIGN

    0x005B: 0x005D,   # LEFT SQUARE BRACKET
    0x005D: 0x005B,   # RIGHT SQUARE BRACKET

    0x007B: 0x007D,   # LEFT CURLY BRACKET
    0x007D: 0x007B,   # RIGHT CURLY BRACKET

    0x00AB: 0x00BB,   # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0x00BB: 0x00AB,   # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
}


def get_mirrored(text):
    return ''.join([
        unichr(MIRROR_MAP.get(ord(char), ord(char))) for char in text
    ])

def get_reversed(text):
    return get_mirrored(reversed(text))
