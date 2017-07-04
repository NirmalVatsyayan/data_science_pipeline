from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#a text example
example_sent = "This is a sample sentence, showing off the stop words filtration."

#all stop words
stop_words = set(stopwords.words('english'))
print("All stop words :: ", len(stop_words))
print(stop_words)
print("\n\n")

#tokenize a sentence
word_tokens = word_tokenize(example_sent)

#filter stop words from sentence tokens using list comprehension
filtered_sentence = [w for w in word_tokens if not w in stop_words]

#filter stop words from sentence tokens using loop
#filtered_sentence = []
#for w in word_tokens:
#    if w not in stop_words:
#        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
