# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
# find files with simillar filenames in Lurkmore and Wikipedia
import os, codecs
import os.path
lurk_mass = []
wiki_mass = []
mass = []
wiki_path = 'D:\\HW_Python\\wiki\\wikipedia_rus\\'
lurk_path = 'D:\\HW_Python\\wiki\\lurkmore\\'
OUTPUT_DIR_1 = 'D:\\HW_Python\\wiki\\dubl\\lurk'
OUTPUT_DIR_2 = 'D:\\HW_Python\\wiki\\dubl\\wiki'

for filename in os.listdir(lurk_path):
    lurk_mass.append(filename.lower())

for filename in os.listdir(wiki_path):
    wiki_mass.append(filename.lower())

for file in lurk_mass:
    if file in wiki_mass:
        fIn_1 = codecs.open(lurk_path + file, 'r', 'utf-8')
        text_1 = fIn_1.read()
        completeName_1 = os.path.join(OUTPUT_DIR_1, file)
        fOut_1 = codecs.open(completeName_1, 'w', 'utf-8')
        fOut_1.write(text_1)
        fOut_1.close()
        fIn_2 = codecs.open(wiki_path + file, 'r', 'utf-8')
        text_2 = fIn_2.read()
        completeName_2 = os.path.join(OUTPUT_DIR_2, file)
        fOut_2 = codecs.open(completeName_2, 'w', 'utf-8')
        fOut_2.write(text_2)
        fOut_2.close()
print ('finished')