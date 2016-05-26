# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
# Splitting Wikipedia articles and delete small files
import os, re, codecs
import os.path
OUTPUT_DIR = 'D:\\HW_Python\\wiki\\new_wiki'

folders = []
path = 'D:\\HW_Python\\wiki\\wiki_extracted'
for foldername in os.listdir(path):
    folders.append(foldername)
for folder in folders:
    print ('making folder -->' + folder + ' ...')
    os.chdir('D:\\HW_Python\\wiki\\wiki_extracted\\' + folder)
    for filename in os.listdir(path + '\\' + folder):
        fIn = codecs.open(filename, 'r', 'utf-8')
        text = fIn.read().replace('\n', ' ')
        m = re.findall('<doc.*?>(.*?)</doc>', text)
        for i in m:
            name = i.split('\r')
            completeName = os.path.join(OUTPUT_DIR, name[1] + '.txt')
            if len(i) > 1000:
                try:
                    fOut = codecs.open(completeName, 'w', 'utf-8')
                    fOut.write(i)
                    fOut.close()
                except:
                    continue
print ('finished')