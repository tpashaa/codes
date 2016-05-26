# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
# Rename Wikipedia articles and delete empty files
import os, re
import os.path
path = 'D:\\HW_Python\\wiki\\new_wiki\\'
OUTPUT_DIR = 'D:\\HW_Python\\wiki\\wikipedia_rus\\'
for filename in os.listdir(path):
    b = os.path.getsize(path + filename)
#    if b == 0:
#        os.remove(path + filename)
    m = re.search(' (.*?txt)', filename)
    if m != None:
        name = m.group(1)
        name = name.replace(', ', '_')
        name = name.replace(' ', '_')
        os.rename(path + filename, OUTPUT_DIR + name)