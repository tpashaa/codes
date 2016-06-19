# -*- coding: utf-8 -*-
import codecs

mass = []
fIn = codecs.open('amh_alf.txt', 'r', 'utf-8')
for line in fIn:
    mass.append(line.strip('\r\n'))

vowels = mass[0].split('\t')
alph = {}
for m in mass[1:]:
    new = m.split('\t')
    alph[new[1]] = vowels[1] + new[0]
    alph[new[2]] = vowels[2] + new[0]
    alph[new[3]] = vowels[3] + new[0]
    alph[new[4]] = vowels[4] + new[0]
    alph[new[5]] = vowels[5] + new[0]
    alph[new[6]] = vowels[6] + new[0]
    alph[new[7]] = vowels[7] + new[0]

ahmar_text = codecs.open('111.txt', 'r', 'utf-8') #input the name of file
fOut = codecs.open('output.txt', 'w', 'utf-8')
for line in ahmar_text:
    for letter in line:
        if letter in alph:
            line = line.replace(letter, alph[letter])
    fOut.write(line)
fOut.close()