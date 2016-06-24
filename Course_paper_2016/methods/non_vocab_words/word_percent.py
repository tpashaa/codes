# -*- coding: utf-8 -*-
import codecs, os, re

path = 'C:\\Users\\Pasha\\Desktop\\курсовая_2016\\mystem\\lurk\\'

per = []
nonwords = []
for filename in os.listdir(path):
    fIn = codecs.open(path + filename, 'r', 'utf-8')
    text = fIn.read()
    text = text.split('\n')
    nonlit = []
    for word in text:
        m = re.search('^(.*?)\?$', word)
        if m != None:
            nonlit.append(m.group(1))
        
    cleared = []
    for i in nonlit:
        m = re.search('^(.*)\?$', i)
        if m == None:
            cleared.append(i)
            nonwords.append(i)
    res = (len(cleared)*100)/len(text)
    per.append(res)
print (sum(per)/len(per))

fOut = codecs.open('lurk_slang.txt', 'w', 'utf-8')
new = []
for i in nonwords:
    if '?' in i:
        n = re.search('(.*?)\?|', i)
        if n != None:
            if n.group(1) not in new:
                new.append(n.group(1))
    else:
        new.append(i)
for i in set(new):
    fOut.write(i + '\n')
fOut.close()