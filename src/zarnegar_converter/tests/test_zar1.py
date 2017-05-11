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

from unittest import TestCase

from zarnegar_converter.zar1_file import Zar1File

class TestZar1(TestCase):
    def test_zar1_text(self):
        sample = Zar1File.get(open('samples/zar1-sample-text-01.zar', 'r'))

        input_lines = sample.get_zar1_text_lines()
        self.assertEqual(input_lines, [
            '                                                          \xf4\x91\xfe\xa1 \x96\x91\xfe\xe4\x91\x93\xa4 \xb4\xf9\xa4\x91\x93\xa4\xa2 |',
            '                                                            \xfc\xf7\x95\x90\xa6 \xa4\xe3\xaa \xa4\xa2 \xf8\xee\xfe\x91\xfb |',
        ])

        zar1_text_lines = sample.get_zar1_text_lines()
        self.assertEqual(zar1_text_lines, [
            '                                                          \xf4\x91\xfe\xa1 \x96\x91\xfe\xe4\x91\x93\xa4 \xb4\xf9\xa4\x91\x93\xa4\xa2 |',
            '                                                            \xfc\xf7\x95\x90\xa6 \xa4\xe3\xaa \xa4\xa2 \xf8\xee\xfe\x91\xfb |',
        ])

        unicode_legacy_lro_lines = sample.get_unicode_legacy_lro_lines()
        self.assertEqual(unicode_legacy_lro_lines, [
            u'‭                                                          ﻡﺎﯾﺧ ﺕﺎﯾﻋﺎﺑﺭ ﻩﺭﺎﺑﺭﺩ |',
            u'‭                                                            ﯽﻧﭘﺍﮊ ﺭﻌﺷ ﺭﺩ ﻭﮐﯾﺎﻫ |',
        ])
