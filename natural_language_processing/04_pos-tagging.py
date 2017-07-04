'''
PunktSentenceTokenizer is a sentence tokenizer like sent_tokenizer
but it is capable of unsupervised machine learning, so we can train it
to any body of text the we use
'''

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#create training and testing data from examples
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

#train the PunktSentenceTokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#tokenize the sample text based upon learning from train text
tokenized = custom_sent_tokenizer.tokenize(sample_text)
print(len(tokenized)) #total sentences generated

def process_content():
    try:
        #to test iterate over a few sentences
        for i in tokenized[:5]:
            #tokenize words from sentence
            words = nltk.word_tokenize(i)
            #do pos tagging
            tagged = nltk.pos_tag(words)
            print(tagged)

    except Exception as e:
        print(str(e))

process_content()
