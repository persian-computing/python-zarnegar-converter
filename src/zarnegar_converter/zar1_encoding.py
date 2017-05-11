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

import logging

from zarnegar_converter import unicode_arabic
from zarnegar_converter import unicode_bidi

"""
Convert Zarnegar Encoding to Unicode Arabic Presentation Form
"""

_AHAIF = unicode_arabic.ARABIC_HAMZA_ABOVE_ISOLATED_FORM_PUA

_IRAN_SYSTEM_MAP = {
    # Numerals
    0x80: 0x06F0,   # EXTENDED ARABIC-INDIC DIGIT ZERO
    0x81: 0x06F1,   # EXTENDED ARABIC-INDIC DIGIT ONE
    0x82: 0x06F2,   # EXTENDED ARABIC-INDIC DIGIT TWO
    0x83: 0x06F3,   # EXTENDED ARABIC-INDIC DIGIT THREE
    0x84: 0x06F4,   # EXTENDED ARABIC-INDIC DIGIT FOUR
    0x85: 0x06F5,   # EXTENDED ARABIC-INDIC DIGIT FIVE
    0x86: 0x06F6,   # EXTENDED ARABIC-INDIC DIGIT SIX
    0x87: 0x06F7,   # EXTENDED ARABIC-INDIC DIGIT SEVEN
    0x88: 0x06F8,   # EXTENDED ARABIC-INDIC DIGIT EIGHT
    0x89: 0x06F9,   # EXTENDED ARABIC-INDIC DIGIT NINE

    # Punctuations
    0x8A: 0x060C,   # ARABIC COMMA
    0x8B: 0x0640,   # ARABIC TATWEEL
    0x8C: 0x061F,   # ARABIC QUESTION MARK

    # Letters
    0x8D: 0xFE81,   # ARABIC LETTER ALEF WITH MADDA ABOVE ISOLATED FORM
    0x8E: 0xFE8B,   # ARABIC LETTER YEH WITH HAMZA ABOVE INITIAL FORM
    0x8F: 0xFE80,   # ARABIC LETTER HAMZA ISOLATED FORM

    0x90: 0xFE8D,   # ARABIC LETTER ALEF ISOLATED FORM
    0x91: 0xFE8E,   # ARABIC LETTER ALEF FINAL FORM
    0x92: 0xFE8F,   # ARABIC LETTER BEH ISOLATED FORM
    0x93: 0xFE91,   # ARABIC LETTER BEH INITIAL FORM
    0x94: 0xFB56,   # ARABIC LETTER PEH ISOLATED FORM
    0x95: 0xFB58,   # ARABIC LETTER PEH INITIAL FORM
    0x96: 0xFE95,   # ARABIC LETTER TEH ISOLATED FORM
    0x97: 0xFE97,   # ARABIC LETTER TEH INITIAL FORM
    0x98: 0xFE99,   # ARABIC LETTER THEH ISOLATED FORM
    0x99: 0xFE9B,   # ARABIC LETTER THEH INITIAL FORM
    0x9A: 0xFE9D,   # ARABIC LETTER JEEM ISOLATED FORM
    0x9B: 0xFE9F,   # ARABIC LETTER JEEM INITIAL FORM
    0x9C: 0xFB7A,   # ARABIC LETTER TCHEH ISOLATED FORM
    0x9D: 0xFB7C,   # ARABIC LETTER TCHEH INITIAL FORM
    0x9E: 0xFEA1,   # ARABIC LETTER HAH ISOLATED FORM
    0x9F: 0xFEA3,   # ARABIC LETTER HAH INITIAL FORM

    0xA0: 0xFEA5,   # ARABIC LETTER KHAH ISOLATED FORM
    0xA1: 0xFEA7,   # ARABIC LETTER KHAH INITIAL FORM
    0xA2: 0xFEA9,   # ARABIC LETTER DAL ISOLATED FORM
    0xA3: 0xFEAB,   # ARABIC LETTER THAL ISOLATED FORM
    0xA4: 0xFEAD,   # ARABIC LETTER REH ISOLATED FORM
    0xA5: 0xFEAF,   # ARABIC LETTER ZAIN ISOLATED FORM
    0xA6: 0xFB8A,   # ARABIC LETTER JEH ISOLATED FORM
    0xA7: 0xFEB1,   # ARABIC LETTER SEEN ISOLATED FORM
    0xA8: 0xFEB3,   # ARABIC LETTER SEEN INITIAL FORM
    0xA9: 0xFEB5,   # ARABIC LETTER SHEEN ISOLATED FORM
    0xAA: 0xFEB7,   # ARABIC LETTER SHEEN INITIAL FORM
    0xAB: 0xFEB9,   # ARABIC LETTER SAD ISOLATED FORM
    0xAC: 0xFEBB,   # ARABIC LETTER SAD INITIAL FORM
    0xAD: 0xFEBD,   # ARABIC LETTER DAD ISOLATED FORM
    0xAE: 0xFEBF,   # ARABIC LETTER DAD INITIAL FORM
    0xAF: 0xFEC1,   # ARABIC LETTER TAH ISOLATED FORM

    # Shadows
    0xB0: 0x2591,   # LIGHT SHADE
    0xB1: 0x2592,   # MEDIUM SHADE
    0xB2: 0x2593,   # DARK SHADE

    # Box Drawings
    0xB3: 0x2502,   # BOX DRAWINGS LIGHT VERTICAL
    0xB4: 0x2524,   # BOX DRAWINGS LIGHT VERTICAL AND LEFT
    0xB5: 0x2561,   # BOX DRAWINGS VERTICAL SINGLE AND LEFT DOUBLE
    0xB6: 0x2562,   # BOX DRAWINGS VERTICAL DOUBLE AND LEFT SINGLE
    0xB7: 0x2556,   # BOX DRAWINGS DOWN DOUBLE AND LEFT SINGLE
    0xB8: 0x2555,   # BOX DRAWINGS DOWN SINGLE AND LEFT DOUBLE
    0xB9: 0x2563,   # BOX DRAWINGS DOUBLE VERTICAL AND LEFT
    0xBA: 0x2551,   # BOX DRAWINGS DOUBLE VERTICAL
    0xBB: 0x2557,   # BOX DRAWINGS DOUBLE DOWN AND LEFT
    0xBC: 0x255D,   # BOX DRAWINGS DOUBLE UP AND LEFT
    0xBD: 0x255C,   # BOX DRAWINGS UP DOUBLE AND LEFT SINGLE
    0xBE: 0x255B,   # BOX DRAWINGS UP SINGLE AND LEFT DOUBLE
    0xBF: 0x2510,   # BOX DRAWINGS LIGHT DOWN AND LEFT

    0xC0: 0x2514,   # BOX DRAWINGS LIGHT UP AND RIGHT
    0xC1: 0x2534,   # BOX DRAWINGS LIGHT UP AND HORIZONTAL
    0xC2: 0x252C,   # BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
    0xC3: 0x251C,   # BOX DRAWINGS LIGHT VERTICAL AND RIGHT
    0xC4: 0x2500,   # BOX DRAWINGS LIGHT HORIZONTAL
    0xC5: 0x253C,   # BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
    0xC6: 0x255E,   # BOX DRAWINGS VERTICAL SINGLE AND RIGHT DOUBLE
    0xC7: 0x255F,   # BOX DRAWINGS VERTICAL DOUBLE AND RIGHT SINGLE
    0xC8: 0x255A,   # BOX DRAWINGS DOUBLE UP AND RIGHT
    0xC9: 0x2554,   # BOX DRAWINGS DOUBLE DOWN AND RIGHT
    0xCA: 0x2569,   # BOX DRAWINGS DOUBLE UP AND HORIZONTAL
    0xCB: 0x2566,   # BOX DRAWINGS DOUBLE DOWN AND HORIZONTAL
    0xCC: 0x2560,   # BOX DRAWINGS DOUBLE VERTICAL AND RIGHT
    0xCD: 0x2550,   # BOX DRAWINGS DOUBLE HORIZONTAL
    0xCE: 0x256C,   # BOX DRAWINGS DOUBLE VERTICAL AND HORIZONTAL
    0xCF: 0x2567,   # BOX DRAWINGS UP SINGLE AND HORIZONTAL DOUBLE

    0xD0: 0x2568,   # BOX DRAWINGS UP DOUBLE AND HORIZONTAL SINGLE
    0xD1: 0x2564,   # BOX DRAWINGS DOWN SINGLE AND HORIZONTAL DOUBLE
    0xD2: 0x2565,   # BOX DRAWINGS DOWN DOUBLE AND HORIZONTAL SINGLE
    0xD3: 0x2559,   # BOX DRAWINGS UP DOUBLE AND RIGHT SINGLE
    0xD4: 0x2558,   # BOX DRAWINGS UP SINGLE AND RIGHT DOUBLE
    0xD5: 0x2552,   # BOX DRAWINGS DOWN SINGLE AND RIGHT DOUBLE
    0xD6: 0x2553,   # BOX DRAWINGS DOWN DOUBLE AND RIGHT SINGLE
    0xD7: 0x256B,   # BOX DRAWINGS VERTICAL DOUBLE AND HORIZONTAL SINGLE
    0xD8: 0x256A,   # BOX DRAWINGS VERTICAL SINGLE AND HORIZONTAL DOUBLE
    0xD9: 0x2518,   # BOX DRAWINGS LIGHT UP AND LEFT
    0xDA: 0x250C,   # BOX DRAWINGS LIGHT DOWN AND RIGHT

    # Shadows
    0xDB: 0x2588,   # FULL BLOCK
    0xDC: 0x2584,   # LOWER HALF BLOCK
    0xDD: 0x258C,   # LEFT HALF BLOCK
    0xDE: 0x2590,   # RIGHT HALF BLOCK
    0xDF: 0x2580,   # UPPER HALF BLOCK

    # Letters
    0xE0: 0xFEC5,   # ARABIC LETTER ZAH ISOLATED FORM
    0xE1: 0xFEC9,   # ARABIC LETTER AIN ISOLATED FORM
    0xE2: 0xFECA,   # ARABIC LETTER AIN FINAL FORM
    0xE3: 0xFECC,   # ARABIC LETTER AIN MEDIAL FORM
    0xE4: 0xFECB,   # ARABIC LETTER AIN INITIAL FORM
    0xE5: 0xFECD,   # ARABIC LETTER GHAIN ISOLATED FORM
    0xE6: 0xFECE,   # ARABIC LETTER GHAIN FINAL FORM
    0xE7: 0xFED0,   # ARABIC LETTER GHAIN MEDIAL FORM
    0xE8: 0xFECF,   # ARABIC LETTER GHAIN INITIAL FORM
    0xE9: 0xFED1,   # ARABIC LETTER FEH ISOLATED FORM
    0xEA: 0xFED3,   # ARABIC LETTER FEH INITIAL FORM
    0xEB: 0xFED5,   # ARABIC LETTER QAF ISOLATED FORM
    0xEC: 0xFED7,   # ARABIC LETTER QAF INITIAL FORM
    0xED: 0xFB8E,   # ARABIC LETTER KEHEH ISOLATED FORM
    0xEE: 0xFB90,   # ARABIC LETTER KEHEH INITIAL FORM
    0xEF: 0xFB92,   # ARABIC LETTER GAF ISOLATED FORM

    # Letters
    0xF0: 0xFB94,   # ARABIC LETTER GAF INITIAL FORM
    0xF1: 0xFEDD,   # ARABIC LETTER LAM ISOLATED FORM
    0xF2: 0xFEFB,   # ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
    0xF3: 0xFEDF,   # ARABIC LETTER LAM INITIAL FORM
    0xF4: 0xFEE1,   # ARABIC LETTER MEEM ISOLATED FORM
    0xF5: 0xFEE3,   # ARABIC LETTER MEEM INITIAL FORM
    0xF6: 0xFEE5,   # ARABIC LETTER NOON ISOLATED FORM
    0xF7: 0xFEE7,   # ARABIC LETTER NOON INITIAL FORM
    0xF8: 0xFEED,   # ARABIC LETTER WAW ISOLATED FORM
    0xF9: 0xFEE9,   # ARABIC LETTER HEH ISOLATED FORM
    0xFA: 0xFEEC,   # ARABIC LETTER HEH MEDIAL FORM
    0xFB: 0xFEEB,   # ARABIC LETTER HEH INITIAL FORM
    0xFC: 0xFBFD,   # ARABIC LETTER FARSI YEH FINAL FORM
    0xFD: 0xFBFC,   # ARABIC LETTER FARSI YEH ISOLATED FORM
    0xFE: 0xFBFE,   # ARABIC LETTER FARSI YEH INITIAL FORM

    0xFF: 0x00A0,   # NO-BREAK SPACE
}

_ZARNEGAR_OVERRIDES_MAP = {
    0x00: 0x0000,
    0x01: 0x0001,

    0x03: 0xFD3E,   # ORNATE LEFT PARENTHESIS
    0x04: 0xFD3F,   # ORNATE RIGHT PARENTHESIS

    0x1D: 0x00A0,   # NO-BREAK SPACE

    0xB0: 0xFE7C,   # ARABIC SHADDA ISOLATED FORM
    0xB1: 0xFE76,   # ARABIC FATHA ISOLATED FORM
    0xB2: 0xFE70,   # ARABIC FATHATAN ISOLATED FORM
    # 0xB3: TODO
    0xB4: _AHAIF,   # ARABIC HAMZA ABOVE ISOLATED FORM
    0xB5: 0xFE78,   # ARABIC DAMMA ISOLATED FORM
    0xB6: 0xFE72,   # ARABIC DAMMATAN ISOLATED FORM
    # 0xB7: TODO
    # 0xB8: TODO
    # 0xB9: TODO
    # 0xBA: TODO
    # 0xBB: TODO
    # 0xBC: TODO
    # 0xBD: TODO
    0xBE: 0xFE7A,   # ARABIC KASRA ISOLATED FORM
    # 0xBF: TODO

    # 0xC0: TODO
    # 0xC1: TODO
    # 0xC2: TODO
    0xC3: 0x00AB,   # LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
    0xC4: 0x00BB,   # RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK
    # 0xC5: TODO
    # 0xC6: TODO
    0xC7: 0x061B,   # ARABIC SEMICOLON
    # 0xC8: TODO
    # 0xC9: TODO
    # 0xCA: TODO
    # 0xCB: TODO
    # 0xCC: TODO
    # 0xCD: TODO
    # 0xCE: TODO
    # 0xCF: TODO
}

_ZARNEGAR_MAP = dict(enumerate(range(0x80)))
_ZARNEGAR_MAP.update(_IRAN_SYSTEM_MAP)
_ZARNEGAR_MAP.update(_ZARNEGAR_OVERRIDES_MAP)


def _in_zar_override(char_byte):
    return ord(char_byte) in _ZARNEGAR_OVERRIDES_MAP

def convert_zar_byte_to_legacy_char(char_byte, line_no):
    codepoints = _ZARNEGAR_MAP[ord(char_byte)]

    if type(codepoints) is int:
        # "U+%04X" % ord(char) if char is not None else "NONE"
        #if ord(char_byte) in range(0x00, 0x20):
        if ord(char_byte) in range(0x00, 0x20) and not _in_zar_override(char_byte):
            logging.error('zar_legacy: ERROR1: Line %4d:   0x%02X', line_no, ord(char_byte))
        #if ord(char_byte) in range(0xB0, 0xE0):
        if ord(char_byte) in range(0xB0, 0xE0) and not _in_zar_override(char_byte):
            logging.error('zar_legacy: ERROR2: Line %4d:   0x%02X', line_no, ord(char_byte))
        return unichr(codepoints)

    if type(codepoints) is list:
        return ''.join(map(lambda cp: unichr(cp), codepoints))

    raise Error("invalid map value")

def convert_zar1_line_to_unicode_legacy_lro(zar1_line, line_no):
    legacy_text = ''.join([
        convert_zar_byte_to_legacy_char(zar_byte, line_no)
        for zar_byte in zar1_line
    ])
    return unicode_bidi.LRO_CHAR + legacy_text

def convert_zar1_line_to_semantic_lro(zar_text, line_no):
    legacy_text = ''.join([
        convert_zar_byte_to_legacy_char(zar_byte, line_no)
        for zar_byte in zar_text
    ])
    return unicode_arabic.convert_legacy_line_to_semantic_lro(legacy_text, line_no)

def convert_zar1_line_to_unicode_lro(zar_text, line_no):
    lro_text = convert_zar1_line_to_semantic_lro(zar_text, line_no)
    return unicode_bidi.LRO_CHAR + lro_text

def convert_zar1_line_to_unicode_rlo(zar_text, line_no):
    lro_text = convert_zar1_line_to_semantic_lro(zar_text, line_no)
    rlo_text = unicode_bidi.get_reversed(lro_text)
    return unicode_bidi.RLO_CHAR + rlo_text
