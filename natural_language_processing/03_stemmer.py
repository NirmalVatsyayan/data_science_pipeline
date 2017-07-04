'''
The idea of stemming is a sort of normalizing method.
Many variations of words carry the same meaning, other than when tense is involved.

Ex: I was taking a ride in the car.
    I was riding in the car.
Both means the same thing.

One of the most popular stemming algorithms is the Porter stemmer, which has been around since 1979.
'''
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

print("Stemming words :: \n\n")
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))

print("Stemming sentences :: \n\n")
new_text = '''It is important to be very pythonly while you are pythoning with python.
All pythoners have pythoned poorly at least once.'''

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
