# -*- coding: utf-8 -*-
import codecs

fIn1 = codecs.open('C:/Users/Pasha/Desktop/ngramms/lurkmore_trigram.txt', 'r', 'utf-8')
fIn2 = codecs.open('C:/Users/Pasha/Desktop/wiki_trigr.txt', 'r', 'utf-8')

lurk = fIn1.read().split('\n')
wiki = fIn2.read().split('\n')

fOut = codecs.open('results_all_trigr.txt', 'w', 'utf-8')
for n in lurk:
    if n not in wiki:
        fOut.write(n + '\n')