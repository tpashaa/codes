# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
# Rename Lurkmore files for further action
import os, re
import os.path

path = 'D:\\HW_Python\\wiki\\lurkmore'
for filename in os.listdir(path):
    m = re.search('.*?(&.*?)\.txt', filename)
    if m != None:
        filename1 = filename.replace(m.group(1), '')
        os.rename(filename, filename1)
