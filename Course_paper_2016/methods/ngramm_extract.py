# -*- coding: utf-8 -*-
import codecs, re, os, nltk, random
import os.path
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

path = 'D:\\HW_Python\\wiki\\dubl\\wiki\\'
stopsignes = [',', '.', '(', ')', '!', '/', '{', '}', '[', ']', ';', ':',
              '\\', '`', '~', '<', '>', '|', '№', '%', '«', '»', '•',
              '■', '□', '×', '...', '”', '·', '``', '£', '®', '©', '…',
              '_', '™', '—', '$', "'s", '?', '&', '--', '’',]

#count words in the corpus
def word_count(path):
    word_num = 0
    for filename in os.listdir(path):
        try:
            fIn = codecs.open(path + filename, 'r', 'utf-8')
            text = fIn.read()    
            words = re.findall('\w+', text)
            word_num += len(words)
        except:
            continue
    return word_num
    
# lurkmore_len = 9877944
# wikipedia_len = 43400921

#lowercase all words, delete signes and tokenize
def preprocess(path, stopsignes):
    files = []
    corpus = []
    for filename in os.listdir(path):
        files.append(filename)
    del files[0]
    random.shuffle(files)
    for filename in files:
        fIn = codecs.open(path + filename, 'r', 'utf-8')
        text = fIn.read().lower()
        for s in stopsignes:
            text = text.replace(s, ' ')
        text = word_tokenize(text)
        for word in text:
            corpus.append(word)
        fIn.close()
    print ('corpus preprocessed...')
    return corpus

corpus = preprocess(path, stopsignes)

#delete stopwords from corpus
stopwords_lurkmore = 'D:/HW_Python/wiki/stopwords_lurk.txt'
def delstops(corpus, stopwords_file):
    cleared = []
    fIn = codecs.open(stopwords_file, 'r', 'utf-8')
    stopw = fIn.read().split('\n')
    for word in corpus:
        if word not in stopw:
            m = re.search('\w+', word)
            if m != None:
                cleared.append(m.group(0))
    print ('stopwords deleted...')
    return cleared

clear_corpus = delstops(corpus, stopwords_lurkmore)

#make frequency list of n-gramms
def freqlist(corpus, num):
    #num - len of n-gramm
    res = []
    if num == 1:
        fd = nltk.FreqDist(corpus)
        for i in fd.most_common(500):
            res.append(i)
    elif num == 2:
        bigr = nltk.bigrams(corpus)
        fd = nltk.FreqDist(bigr)
        for i in fd.most_common(500):
            res.append(i)
    else:
        ngram = ngrams(corpus, num)
        fd = nltk.FreqDist(ngram)
        for i in fd.most_common(500):
            res.append(i)
    return res
            

num = input('Input the length of n-grams: ')
res = freqlist(clear_corpus, int(num))
for i in res:
    print (i)