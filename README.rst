===============================================================
Converter for Zarnegar Encoding and File Format to Unicode Text
===============================================================

Homepage: https://github.com/behnam/python-zarnegar-converter

`Zarnegar`_ (Persian: *زرنگار*, zarnegār, meaning gold-depicting) is a
commercial, stand-alone Persian/Arabic word processor program developed for
MS-DOS and Windows.  The first version of Zarnegar (for DOS), was released in
April-May 1991, and Windows versions have been available since 2000.

Zarnegar has employed two different character sets and file formats.

-----------------------
Zarnegar1 Character Set
-----------------------

Zarnegar used an `Iran System`_-based character encoding system, named
*Zarnegar1*, with text file formats for its early versions, up to its "Zarnegar
75" version.  *Zarnegar1* character set is a *2-form left-to-right visual
encoding*, meaning the every `Perso-Arabic`_ letter receives different
character codes based on its cursive joining form, but most letters receive
only 2 forms, because of the limited code-points available2 forms, because of
the limited code-points available.

This project has a partial implementation of `Zarnegar1`_ encoding
(`zarnegar_converter/zar1_encoding.py`) and a full implementation of its binary
and text file formats (`zarnegar_converter/zar1_file.py`).

------------------------
Zarnegar75 Character Set
------------------------

With "Zarnegar 75" version of the program, a new character encoding system was
introduced, and the file format was changed to another binary format.
*Zarnegar75* character set is a 4-form bidirectional encoding, meaning that
every `Perso-Arabic`_ letter receives one, two, or four character code,
depending on its cursive joining form, and these letters are stored in the
memory in the semantic order.

Support for *Zarnegar75* file format and encoding is still in progress.

----------
How to Use
----------

.. code:: bash

  $ zarnegar_converter/converter.py unicode_legacy_lro samples/zar1-sample-text-01.zar
  ‭                                                          ﻡﺎﯾﺧ ﺕﺎﯾﻋﺎﺑﺭ ﻩﺭﺎﺑﺭﺩ |
  ‭                                                            ﯽﻧﭘﺍﮊ ﺭﻌﺷ ﺭﺩ ﻭﮐﯾﺎﻫ |

-----------------
How to Contribute
-----------------

Please report any issues at
<https://github.com/behnam/python-zarnegar-converter/issues> or submit GitHub
pull requests.

The encoding mappings (both Zarnegar1 and Zarnegar75) can be improved with
access to more sample files. Please write to <behnam@zwnj.org> if you like to
contribute (private or public) Zarnegar source files to improve this project.

----------------
Acknowledgements
----------------

Thanks to `Cecil H. Green Library`_ of Stanford University, specially John A
Eilts and Behzad Allahyar, for sharing their collection of Zarnegar documents.

Also thanks to `The Official Website of Ahmad Shamlou`_ for sharing their
collection of documents.

------------
Legal Notice
------------

*Zarnegar* is a trademark of *SinaSoft Corporation*. This project is NOT
affiliated with SinaSoft Corporation.

Copyright (C) 2017  Behnam Esfahbod

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

.. _Zarnegar: https://en.wikipedia.org/wiki/Zarnegar_(word_processor)
.. _Zarnegar1: https://en.wikipedia.org/wiki/Zarnegar1
.. _Iran System: https://en.wikipedia.org/wiki/Iran_System_encoding
.. _Perso-Arabic: https://en.wikipedia.org/wiki/Perso-Arabic
.. _Cecil H. Green Library: https://library.stanford.edu/green
.. _The Official Website of Ahmad Shamlou: http://shamlou.org/
