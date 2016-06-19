# -*- coding: utf-8 -*-
import codecs

fIn = codecs.open('georgian.txt', 'r', 'utf-8')
fOut = codecs.open('output.txt', 'w', 'utf-8')

alph = {'ა':'ɑ','ბ':'b','გ':'g','დ':'d','ე':'ɛ','ვ':'v','ზ':'z','ჱ':'ɛj',
           'თ':'tʰ','ი':'i','კ':'k\'','ლ':'l','მ':'m','ნ':'n','ჲ':'j',
           'ო':'ɔ','პ':'p\'','ჟ':'ʒ','რ':'r','ს':'s','ტ':'t\'','ჳ':'wi',
           'უ':'u','ფ':'pʰ','ქ':'kʰ','ღ':'ʁ','ყ':'q\'','შ':'ʃ','ჩ':'tʃ',
           'ც':'ts','ძ':'dz','წ':'tsʼ','ჭ':'tʃʼ','ხ':'χ','ჴ':'q','ჯ':'dʒ',
           'ჰ':'h','ჵ':'hɔɛ'}

for line in fIn:
    for letter in line:
        if letter in alph:
            line = line.replace(letter, alph[letter])
    fOut.write(line)
fOut.close()