from pathlib import Path
import unicodedata
import hebrew_letters
import hebrew_punctuation
from collections import defaultdict
import json

MISSING = defaultdict(int)
NOT_MISSING = 0

def handle_word(word: str):
    global NOT_MISSING
    hebrew_chars_dict = {char: True for char in hebrew_letters.chars + hebrew_punctuation.chars}
    
    word = unicodedata.normalize('NFD', word)
    if len(word) > 30:
        MISSING[word] += 1
        return
    for c in word:
        
        if not hebrew_chars_dict.get(c):
            MISSING[word] += 1
            return
    NOT_MISSING += 1
            

path = Path(__file__).parent / 'data'
files = [i for i in path.glob('**/*.txt') if i.is_file()]
files_count = len(files)

counter = 0
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                handle_word(word)
    counter += 1
    print(f'Done ({counter}/{files_count})')
with open('missing.json', 'w', encoding='utf-8') as f:
    MISSING = dict(sorted(MISSING.items(), key=lambda item: item[1]))
    json.dump(MISSING, f, indent=4, ensure_ascii=False)
    
print(NOT_MISSING)