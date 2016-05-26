# -*- coding: utf-8 -*-
"""
@author: Pasha Taratynov
"""
import os, codecs, re
import os.path
wiki_path = 'D:\\HW_Python\\wiki\\wikipedia_rus\\'
lurk_path = 'D:\\HW_Python\\wiki\\lurkmore\\'
OUTPUT_DIR = 'D:\\HW_Python\\wiki\\dubl\\people\\'

names = ['Владимир', 'Алексей', 'Павел', 'Игорь', 'Станислав', 'Сергей', \
'Александр', 'Андрей', 'Борис', 'Татьяна', 'Анастасия', 'Ольга', 'Надежда', \
'Людмила', 'Анна', 'Елена', 'Маргарита', 'Ирина', 'Мария', 'Дмитрий', 'Олег', \
'Кирилл', 'Jimi', 'Jimmy', 'Justin', 'Антон', 'Арсений', 'Валерия', 'Виктор', \
'Геннадий', 'Георгий', 'Евгений', 'Иван', 'Илья', 'Николай', 'Петр']

for filename in os.listdir(lurk_path):
    for i in names:
        name = '(' + i + ')' + '_(.*?).txt'
        m = re.search(name, filename)
        if m != None:
            if '_' not in m.group(2):
                for filename_2 in os.listdir(wiki_path):
                    if m.group(1) in filename_2 and m.group(2) in filename_2:
                        fIn_1 = codecs.open(lurk_path + filename, 'r', 'utf-8')
                        text_1 = fIn_1.read()
                        completeName_1 = os.path.join(OUTPUT_DIR, m.group(2) + \
                        '_' + m.group(1) + '_lurk.txt')
                        fOut_1 = codecs.open(completeName_1, 'w', 'utf-8')
                        fOut_1.write(text_1)
                        fOut_1.close()
                        fIn_2 = codecs.open(wiki_path + filename_2, 'r', 'utf-8')
                        text_2 = fIn_2.read()
                        completeName_2 = os.path.join(OUTPUT_DIR, filename_2)
                        fOut_2 = codecs.open(completeName_2, 'w', 'utf-8')
                        fOut_2.write(text_2)
                        fOut_2.close()
                        print ('Done')
print ('finished')