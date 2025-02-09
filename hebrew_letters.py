r"""
All characters in Hebrew that used for LETTERS sounds
Excluding Gershaim (0x22 and 0x5F4) as it's not sound in character level
Excluding RAFE (0x5BF), METEG (0x5BD)
Checked on ~3M words curpos

Reference 
    https://en.wikipedia.org/wiki/Unicode_and_HTML_for_the_Hebrew_alphabet#Compact_table
    https://en.wikipedia.org/wiki/Hebrew_punctuation#Geresh_and_gershayim
    https://github.com/python/cpython/blob/main/Lib/string.py#L31
    
For display the name of each use:
import unicodedata
unicodedata.name(c)

To normalize hebrew characters (eg. U+FB4x from single character of letter + nikud into multiple characters).
import unicodedata
unicodedata.normalize('NFD', '\uFB30')
"""

chars = []
chars.extend(list('אבגדהוזחטיכלמנסעפצקרשת')) # Alef - Taf
chars.extend(list('ךםןףץ')) # Sofiyot    
# Nikud U+05Bx and U+05Cx
chars.extend([
    '\u05B0', # SHEVA
    '\u05B1', # HATAF SEGOL
    '\u05B2', # HATAF PATAH
    '\u05B3', # HATAF QAMATS
    '\u05B4', # HIRIQ
    '\u05B5', # TSERE
    '\u05B6', # SEGOL
    '\u05B7', # PATAH
    '\u05B8', # QAMATS
    '\u05B9', # HOLAM
    '\u05BA', # HOLAM HASER FOR VAV
    '\u05BB', # QUBUTS
    '\u05BC', # DAGESH OR MAPIQ
    
    '\u05C1', # SHIN DOT
    '\u05C2', # SIN DOT
    
    '\u05C7', # QAMATS QATAN
])
# Special characters added to letters
chars.append('\u0027') # APOSTROPHE like in Jirafa