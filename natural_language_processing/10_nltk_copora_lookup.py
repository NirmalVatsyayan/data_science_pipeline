import os
import sys
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg

print(nltk.__file__)

path = []

if sys.platform.startswith('win'):
    # Common locations on Windows:
    path += [
        str(r'C:\nltk_data'), str(r'D:\nltk_data'), str(r'E:\nltk_data'),
        os.path.join(sys.prefix, str('nltk_data')),
        os.path.join(sys.prefix, str('lib'), str('nltk_data')),
        os.path.join(os.environ.get(str('APPDATA'), str('C:\\')), str('nltk_data'))
    ]
else:
    # Common locations on UNIX & OS X:
    path += [
        str('/usr/share/nltk_data'),
        str('/usr/local/share/nltk_data'),
        str('/usr/lib/nltk_data'),
        str('/usr/local/lib/nltk_data')
    ]

print(path)

# sample text
sample = gutenberg.raw("bible-kjv.txt")

tok = sent_tokenize(sample)

for x in range(5):
    print(tok[x])
