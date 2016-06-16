# -*- coding: utf-8 -*-
import codecs, re, os, nltk
import os.path
from nltk.tokenize import word_tokenize
from nltk.util import ngrams


path = 'C:\\Users\\Pasha\\Documents\\GitHub\\codes\\Wikipedia_HW\\wiki_extracted\\'
stopsignes = [',', '.', '(', ')', '!', '/', '{', '}', '[', ']', ';', ':',
              '\\', '`', '~', '<', '>', '|', '№', '%', '«', '»', '•',
              '■', '□', '×', '...', '”', '·', '``', '£', '®', '©', '…',
              '_', '™', '—', '$', "'s", '?', '&', '--', '’',]

#lowercase all words, delete signes and tokenize
def preprocess(path, stopsignes):
    files = []
    corpus = []
    for filename in os.listdir(path):
        files.append(filename)
    del files[0]
    for filename in files:
        print (filename)
        fIn = codecs.open(path + filename, 'r', 'utf-8')
        text = fIn.read().lower()
        for s in stopsignes:
            text = text.replace(s, ' ')
        text = word_tokenize(text)
        for word in text:
            corpus.append(word)
    print ('corpus preprocessed...')
    return corpus

#delete stopwords from corpus
stopwords = 'C:/Users/Pasha/Documents/GitHub/codes/Wikipedia_HW/stopwords.txt'
def delstops(corpus, stopwords_file):
    cleared = []
    fIn = codecs.open(stopwords_file, 'r', 'utf-8')
    stopw = fIn.read().split('\n')
    for word in corpus:
        if word not in stopw:
            cleared.append(word)
    print ('stopwords deleted...')
    return cleared

#make frequency list of n-gramms
def freqlist(corpus, num):
    #num - len of n-gramm
    res = []
    if num == 1:
        fd = nltk.FreqDist(corpus)
        for i in fd.most_common(100):
            res.append(i)
    elif num == 2:
        bigr = nltk.bigrams(corpus)
        fd = nltk.FreqDist(bigr)
        for i in fd.most_common(100):
            res.append(i)
    else:
        ngram = ngrams(corpus, num)
        fd = nltk.FreqDist(ngram)
        for i in fd.most_common(100):
            res.append(i)
    return res
            
corpus = preprocess(path, stopsignes)
clear_corpus = delstops(corpus, stopwords)

num = input('Input the length of n-grams: ')
res = freqlist(clear_corpus, int(num))
fOut = codecs.open('result.txt', 'w', 'utf-8')
for i in res:
    m = re.search('\w+', i[0])
    if m!= None:
        fOut.write(m.group(0) + '\n')
fOut.close()
