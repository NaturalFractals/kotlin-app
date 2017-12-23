import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import math

example = "This is an example sentence! However, it " \
          "is a very informative one,"

print(word_tokenize(example, language='english'))

tokenizer = RegexpTokenizer(r'\w+')
print(tokenizer.tokenize(example))

all_words_pos = []
with open("pos_crypto.txt", "r", encoding='utf-8',
          errors='ignore') as f_pos:
    for line in f_pos.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_pos.append(w.lower())

pos_res = nltk.FreqDist(all_words_pos)
print(pos_res.most_common(8))

all_words_neg = []
with open("neg_crypto.txt", "r", encoding='utf-8',
          errors='ignore') as f_neg:
    for line in f_neg.readlines():
        words = tokenizer.tokenize(line)
        for w in words:
            if w.lower() not in stop_words:
                all_words_neg.append(w.lower())