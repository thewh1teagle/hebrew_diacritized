import string, unicodedata, re
from pathlib import Path

whitelist = set(string.punctuation + ' \n' + ''.join(chr(c) for c in range(0x5B0, 0x5EB)))
out_whitelist = set(''.join(chr(c) for c in range(0x5B0, 0x5EB)) + """ \n,.?!'""")
path = 'hebrew_diacritized.txt'
files = Path('./data').glob('**/*.txt')

def normalize(text: str):
    text = re.sub('[-+]', ' ', text)
    text = re.sub('[ +]', ' ', text)
    text = re.sub('[.+]', '.', text)
    text = unicodedata.normalize('NFD', text)
    return text

with open(path, 'w') as f:
    for file in files:
        with open(file, 'r') as f1:
            for line in f1:
                line = normalize(line)
                if all(c in whitelist for c in line):
                    line = ''.join(c for c in line if c in out_whitelist)
                    line = line.strip()
                    if line:
                        f.write(line + '\n')
                

    