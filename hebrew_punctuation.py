r"""
All characters in Hebrew that used for punctuation.
Checked on ~3M words curpos

Reference 
    https://en.wikipedia.org/wiki/Hebrew_punctuation#Geresh_and_gershayim
    https://github.com/python/cpython/blob/main/Lib/string.py#L31
"""

import string


chars = []
chars.extend(string.digits + string.punctuation + string.whitespace)
chars.append('\u05F3') # HEBREW PUNCTUATION GERESH
