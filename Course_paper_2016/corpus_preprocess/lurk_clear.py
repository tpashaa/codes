# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
# Clear Lurkmore corpus
import codecs, os
import os.path

bad1 = 'lurkmo.re • lurkmore.co • lurkmore.net • IPv6.lurkmo.re • IPv6.lurkmore.to • friGate • Средства против цензуры • Пожертвования '
bad2 = 'Ужоснах. Статью перепилить.Ужоснах. Статью перепилить.Ужоснах.'
OUTPUT_DIR = 'D:\\HW_Python\\wiki\\lurkmore'


files = []
path = 'D:\\HW_Python\\wiki\\lurk_extracted'
for filename in os.listdir(path):
    files.append(filename)
length = []
deleted = []
for file in files:
    fIn = codecs.open(file, 'r', 'utf-8')
    text = fIn.read()
    if len(text) not in length:
        length.append(len(text))
        if bad1 in text and bad2 not in text:
            completeName = os.path.join(OUTPUT_DIR, file)
            fOut = codecs.open(completeName, 'w', 'utf-8')
            fOut.write(text)
            fOut.close()
        else:
            deleted.append(file)
    else:
        deleted.append(file)

#deletedname = os.path.join('D:\\HW_Python\\wiki', 'OUTPUT_DELETED.txt')
#fOut = codecs.open(deletedname, 'w', 'utf-8')
#for i in deleted:
#    fOut.write(i + '\n')
#fOut.close()