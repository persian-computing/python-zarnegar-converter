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
Unicode Arabic Joining helpers for Zarnegar Encoding
"""


ZWNJ = 0x200C # ZERO-WIDTH NON-JOINER
ZWJ = 0x200D # ZERO-WIDTH JOINER

ZWNJ_CHAR = "\u200C" # ZERO-WIDTH NON-JOINER
ZWJ_CHAR = "\u200D" # ZERO-WIDTH JOINER

LEFT_JOINER = [
    0x0626,   # ARABIC LETTER YEH WITH HAMZA ABOVE
    0x0628,   # ARABIC LETTER BEH
    0x062A,   # ARABIC LETTER TEH
    0x062B,   # ARABIC LETTER THEH
    0x062C,   # ARABIC LETTER JEEM
    0x062D,   # ARABIC LETTER HAH
    0x062E,   # ARABIC LETTER KHAH
    0x0633,   # ARABIC LETTER SEEN
    0x0634,   # ARABIC LETTER SHEEN
    0x0635,   # ARABIC LETTER SAD
    0x0636,   # ARABIC LETTER DAD
    0x0637,   # ARABIC LETTER TAH
    0x0638,   # ARABIC LETTER ZAH
    0x0639,   # ARABIC LETTER AIN
    0x063A,   # ARABIC LETTER GHAIN
    0x0640,   # ARABIC TATWEEL
    0x0641,   # ARABIC LETTER FEH
    0x0642,   # ARABIC LETTER QAF
    0x0644,   # ARABIC LETTER LAM
    0x0645,   # ARABIC LETTER MEEM
    0x0646,   # ARABIC LETTER NOON
    0x0647,   # ARABIC LETTER HEH
    0x067E,   # ARABIC LETTER PEH
    0x0686,   # ARABIC LETTER TCHEH
    0x06A9,   # ARABIC LETTER KEHEH
    0x06AF,   # ARABIC LETTER GAF
    0x06CC,   # ARABIC LETTER FARSI YEH
    ZWJ,
]

RIGHT_JOINER = [
    0x0622,   # ARABIC LETTER ALEF WITH MADDA ABOVE
    0x0626,   # ARABIC LETTER YEH WITH HAMZA ABOVE
    0x0627,   # ARABIC LETTER ALEF
    0x0628,   # ARABIC LETTER BEH
    0x062A,   # ARABIC LETTER TEH
    0x062B,   # ARABIC LETTER THEH
    0x062C,   # ARABIC LETTER JEEM
    0x062D,   # ARABIC LETTER HAH
    0x062E,   # ARABIC LETTER KHAH
    0x062F,   # ARABIC LETTER DAL
    0x0630,   # ARABIC LETTER THAL
    0x0631,   # ARABIC LETTER REH
    0x0632,   # ARABIC LETTER ZAIN
    0x0633,   # ARABIC LETTER SEEN
    0x0634,   # ARABIC LETTER SHEEN
    0x0635,   # ARABIC LETTER SAD
    0x0636,   # ARABIC LETTER DAD
    0x0637,   # ARABIC LETTER TAH
    0x0638,   # ARABIC LETTER ZAH
    0x0639,   # ARABIC LETTER AIN
    0x063A,   # ARABIC LETTER GHAIN
    0x0640,   # ARABIC TATWEEL
    0x0641,   # ARABIC LETTER FEH
    0x0642,   # ARABIC LETTER QAF
    0x0644,   # ARABIC LETTER LAM
    0x0645,   # ARABIC LETTER MEEM
    0x0646,   # ARABIC LETTER NOON
    0x0647,   # ARABIC LETTER HEH
    0x0648,   # ARABIC LETTER WAW
    0x067E,   # ARABIC LETTER PEH
    0x0686,   # ARABIC LETTER TCHEH
    0x0698,   # ARABIC LETTER JEH
    0x06A9,   # ARABIC LETTER KEHEH
    0x06AF,   # ARABIC LETTER GAF
    0x06CC,   # ARABIC LETTER FARSI YEH
    ZWJ,
]


def is_zwnj(char):
    return ord(char) == ZWNJ if char is not None else False

def is_zwj(char):
    return ord(char) == ZWJ if char is not None else False

def is_left_joiner(char):
    return ord(char) in LEFT_JOINER if char is not None else False

def is_right_joiner(char):
    return ord(char) in RIGHT_JOINER if char is not None else False

# Applies to a Left-to-Right text
def remove_useless_joining_control_chars(text):
    result = ''
    text = text.replace(ZWNJ_CHAR + ZWNJ_CHAR, ZWNJ_CHAR)
    text = text.replace(ZWJ_CHAR + ZWJ_CHAR, ZWJ_CHAR)
    text_len = len(text)
    for idx in range(text_len):
        chr_on_left = text[idx - 1] if idx > 0 else None
        chr_current = text[idx]
        chr_on_right = text[idx + 1] if idx < text_len - 1 else None
        if is_zwnj(chr_current):
            if not (is_right_joiner(chr_on_left) and is_left_joiner(chr_on_right)):
                continue
        if is_zwj(chr_current):
            if is_right_joiner(chr_on_left) and is_left_joiner(chr_on_right):
                continue
        result += chr_current
    return result
