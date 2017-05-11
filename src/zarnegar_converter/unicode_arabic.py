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

from zarnegar_converter import unicode_bidi
from zarnegar_converter.unicode_joining import remove_useless_joining_control_chars, ZWNJ, ZWJ as ZWJ_


"""
Convert Unicode Arabic Presentation Form to semantic Unicode Arabic
"""

# U+ARABIC HAMZA ABOVE U+0654 does not have any presentation form encoded in
# the Unicode, therefore we use a PUA code point here.
#
# See also: http://www.unicode.org/L2/L2017/17149-hamza-above-isolated.pdf
ARABIC_HAMZA_ABOVE_ISOLATED_FORM_PUA = 0xF8FD
_AHAIF = ARABIC_HAMZA_ABOVE_ISOLATED_FORM_PUA

_LEGACY_TO_SEMANTIC_MAP = {
    # 1-Shape Letters
    0xFB8A: 0x0698,   # ARABIC LETTER JEH
    0xFE80: 0x0621,   # ARABIC LETTER HAMZA
    0xFEA9: 0x062F,   # ARABIC LETTER DAL
    0xFEAB: 0x0630,   # ARABIC LETTER THAL
    0xFEAD: 0x0631,   # ARABIC LETTER REH
    0xFEAF: 0x0632,   # ARABIC LETTER ZAIN
    0xFEC1: 0x0637,   # ARABIC LETTER TAH
    0xFEC5: 0x0638,   # ARABIC LETTER ZAH
    0xFEED: 0x0648,   # ARABIC LETTER WAW

    # 2-Shape Letters: ALEF
    0xFE8D: [0x0627, ZWNJ],   # ARABIC LETTER ALEF (isolated form)
    0xFE8E: [0x0627, ZWJ_],   # ARABIC LETTER ALEF (final form)

    # 2-Shape Letters: Others
    0xFE8F: [ZWNJ, 0x0628],   # ARABIC LETTER BEH (final-isolated form)
    0xFE91: [ZWJ_, 0x0628],   # ARABIC LETTER BEH (initial-medial form)

    0xFB56: [ZWNJ, 0x067E],   # ARABIC LETTER PEH (final-isolated form)
    0xFB58: [ZWJ_, 0x067E],   # ARABIC LETTER PEH (initial-medial form)

    0xFE95: [ZWNJ, 0x062A],   # ARABIC LETTER TEH (final-isolated form)
    0xFE97: [ZWJ_, 0x062A],   # ARABIC LETTER TEH (initial-medial form)

    0xFE99: [ZWNJ, 0x062B],   # ARABIC LETTER THEH (final-isolated form)
    0xFE9B: [ZWJ_, 0x062B],   # ARABIC LETTER THEH (initial-medial form)

    0xFE9D: [ZWNJ, 0x062C],   # ARABIC LETTER JEEM (final-isolated form)
    0xFE9F: [ZWJ_, 0x062C],   # ARABIC LETTER JEEM (initial-medial form)

    0xFB7A: [ZWNJ, 0x0686],   # ARABIC LETTER TCHEH (final-isolated form)
    0xFB7C: [ZWJ_, 0x0686],   # ARABIC LETTER TCHEH (initial-medial form)

    0xFEA1: [ZWNJ, 0x062D],   # ARABIC LETTER HAH (final-isolated form)
    0xFEA3: [ZWJ_, 0x062D],   # ARABIC LETTER HAH (initial-medial form)

    0xFEA5: [ZWNJ, 0x062E],   # ARABIC LETTER KHAH (final-isolated form)
    0xFEA7: [ZWJ_, 0x062E],   # ARABIC LETTER KHAH (initial-medial form)

    0xFEB1: [ZWNJ, 0x0633],   # ARABIC LETTER SEEN (final-isolated form)
    0xFEB3: [ZWJ_, 0x0633],   # ARABIC LETTER SEEN (initial-medial form)

    0xFEB5: [ZWNJ, 0x0634],   # ARABIC LETTER SHEEN (final-isolated form)
    0xFEB7: [ZWJ_, 0x0634],   # ARABIC LETTER SHEEN (initial-medial form)

    0xFEB9: [ZWNJ, 0x0635],   # ARABIC LETTER SAD (final-isolated form)
    0xFEBB: [ZWJ_, 0x0635],   # ARABIC LETTER SAD (initial-medial form)

    0xFEBD: [ZWNJ, 0x0636],   # ARABIC LETTER DAD (final-isolated form)
    0xFEBF: [ZWJ_, 0x0636],   # ARABIC LETTER DAD (initial-medial form)

    0xFED1: [ZWNJ, 0x0641],   # ARABIC LETTER FEH (final-isolated form)
    0xFED3: [ZWJ_, 0x0641],   # ARABIC LETTER FEH (initial-medial form)

    0xFED5: [ZWNJ, 0x0642],   # ARABIC LETTER QAF (final-isolated form)
    0xFED7: [ZWJ_, 0x0642],   # ARABIC LETTER QAF (initial-medial form)

    0xFB8E: [ZWNJ, 0x06A9],   # ARABIC LETTER KEHEH (final-isolated form)
    0xFB90: [ZWJ_, 0x06A9],   # ARABIC LETTER KEHEH (initial-medial form)

    0xFB92: [ZWNJ, 0x06AF],   # ARABIC LETTER GAF (final-isolated form)
    0xFB94: [ZWJ_, 0x06AF],   # ARABIC LETTER GAF (initial-medial form)

    0xFEDD: [ZWNJ, 0x0644],   # ARABIC LETTER LAM (final-isolated form)
    0xFEDF: [ZWJ_, 0x0644],   # ARABIC LETTER LAM (initial-medial form)

    0xFEE1: [ZWNJ, 0x0645],   # ARABIC LETTER MEEM (final-isolated form)
    0xFEE3: [ZWJ_, 0x0645],   # ARABIC LETTER MEEM (initial-medial form)

    0xFEE5: [ZWNJ, 0x0646],   # ARABIC LETTER NOON (final-isolated form)
    0xFEE7: [ZWJ_, 0x0646],   # ARABIC LETTER NOON (initial-medial form)

    # 3-Shape Letters
    0xFEE9: [ZWNJ, 0x0647],         # ARABIC LETTER HEH (final-isolated form)
    0xFEEB: [ZWJ_, 0x0647, ZWNJ],   # ARABIC LETTER HEH (initial form)
    0xFEEC: [ZWJ_, 0x0647, ZWJ_],   # ARABIC LETTER HEH (medial form)

    0xFBFC: [ZWNJ, 0x06CC, ZWNJ],   # ARABIC LETTER FARSI YEH (isolated form)
    0xFBFD: [ZWNJ, 0x06CC, ZWJ_],   # ARABIC LETTER FARSI YEH (final form)
    0xFBFE: [ZWJ_, 0x06CC],         # ARABIC LETTER FARSI YEH (initial-medial form)

    # 4-Shape Letters
    0xFEC9: [ZWNJ, 0x0639, ZWNJ],   # ARABIC LETTER AIN (isolated form)
    0xFECA: [ZWNJ, 0x0639, ZWJ_],   # ARABIC LETTER AIN (final form)
    0xFECB: [ZWJ_, 0x0639, ZWNJ],   # ARABIC LETTER AIN (initial form)
    0xFECC: [ZWJ_, 0x0639, ZWJ_],   # ARABIC LETTER AIN (medial form)

    0xFECD: [ZWNJ, 0x063A, ZWNJ],   # ARABIC LETTER GHAIN (isolated form)
    0xFECE: [ZWNJ, 0x063A, ZWJ_],   # ARABIC LETTER GHAIN (final form)
    0xFECF: [ZWJ_, 0x063A, ZWNJ],   # ARABIC LETTER GHAIN (initial form)
    0xFED0: [ZWJ_, 0x063A, ZWJ_],   # ARABIC LETTER GHAIN (medial form)

    # Others Letters
    0xFE81: [0x0622, ZWNJ],     # ARABIC LETTER ALEF WITH MADDA ABOVE (isolated form)
    0xFE8B: [ZWJ_, 0x0626],     # ARABIC LETTER YEH WITH HAMZA ABOVE (initial-medial form)
    0xFEFB: [0x0627, 0x0644],   # ARABIC LIGATURE LAM WITH ALEF

    # Diacritics
    0xFE70: 0x064B, # ARABIC FATHATAN (mark)
    0xFE72: 0x064C, # ARABIC DAMMATAN (mark)
    0xFE76: 0x064E, # ARABIC FATHA (mark)
    0xFE78: 0x064F, # ARABIC DAMMA (mark)
    0xFE7A: 0x0650, # ARABIC KASRA (mark)
    0xFE7C: 0x0651, # ARABIC SHADDA (mark)
    0xFE7E: 0x0652, # ARABIC SUKUN (mark)
    _AHAIF: 0x0654, # ARABIC HAMZA ABOVE (mark)
}


def convert_legacy_char_to_semantic_lro(legacy_char, line_no):
    codepoints = _LEGACY_TO_SEMANTIC_MAP.get(ord(legacy_char), ord(legacy_char))
    if type(codepoints) is int:
        return unichr(codepoints)
    if type(codepoints) is list:
        return ''.join(map(lambda cp: unichr(cp), codepoints))
    raise Error("invalid map value")

def convert_legacy_line_to_semantic_lro(legacy_text, line_no):
    semantic_text = ''.join([
        convert_legacy_char_to_semantic_lro(legacy_char, line_no)
        for legacy_char in legacy_text
    ])
    return remove_useless_joining_control_chars(semantic_text)
