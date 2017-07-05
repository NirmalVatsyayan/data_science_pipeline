'''
WordNet is a lexical database for the English language, which was created by Princeton, and is part of the NLTK corpus.
We can use WordNet alongside the NLTK module to find the meanings of words, synonyms, antonyms, and more.
'''
from nltk.corpus import wordnet

syns = wordnet.synsets("program")
print(type(syns))

print(syns)

print(syns[0].name())
print(syns[0].lemmas())
print(syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())

synonyms = []
antonyms = []

#getting synonyms and antonyms
#iterate on synsets
for syn in wordnet.synsets("good"):
    #iterate on the lemmas
    for l in syn.lemmas():
        #add lemmas on sysnonym
        synonyms.append(l.name())
        #if lemmas have antonyms
        if l.antonyms():
            #add antonyms
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#similarity between 2 words
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))
