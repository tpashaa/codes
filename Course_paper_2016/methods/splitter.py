# -*- coding: utf-8 -*-
import nltk.data, codecs, re, os, random

#подгружаем модель для русского языка в nltk_splitter
rus_splitter = nltk.data.load('C:/Users/Pasha/Desktop/курсовая_2016/train_punkt-master/russian.pickle')

path = 'D:\\HW_Python\\wiki\\lurkmore\\'

files = []
for filename in os.listdir(path):
        files.append(filename)
random.shuffle(files)

counter = 0
mass = []
for filename in files[0:2000]:
    if filename != '.DS_Store':
        counter += 1
        summ = 0
        fIn = codecs.open(path + filename, 'r', 'utf-8')
        text = fIn.read()
        res = rus_splitter.tokenize(text)
        for i in res:
            count = len(re.findall(r'\w+', i))
            summ += count
        aver = round(summ/len(res), 3)
        mass.append(aver)

num = sum(mass)
print (round(num/len(mass), 3))