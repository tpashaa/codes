# -*- coding: utf-8 -*-

import codecs, re

def china_dict_preprocess(text):
    new_text = []
    for i in text:
        if i[0] != '#':
            new_text.append(i)
    del new_text[0]
    return new_text

def china_dictionary(array):
    china_dict = []
    for i in array:
        m = re.search('(.*?) (.*?) (\[.*?\]) (/.*/)', i)
        if m != None:
            china_dict.append([m.group(1), m.group(2), m.group(3), m.group(4)])
    return china_dict

def sent_extract(text):
    china_sent = []
    punkt = ['！', '。', '？', '，']
    m = re.findall('<se>(.*?)</se>', chinese)
    for i in m:
        for a in i:
            if a == '“' or a == '”':
                i = i.replace(a, '')
            if a in punkt:
                i = i.replace(a, ' ')
        china_sent.append(i)
    return china_sent


fIn = codecs.open('cedict_ts.u8', 'r', 'utf-8')
text = fIn.read().split('\r\n')
new = china_dict_preprocess(text)

china_dict = china_dictionary(new)
        
fIn2 = codecs.open('stal.xml', 'r', 'utf-8')
chinese = fIn2.read()
sents = sent_extract(chinese)

words = []
for word in china_dict:
    words.append(word[1])

fOut = codecs.open('chinese_HW.xml', 'w', 'utf-8')
fOut.write('<?xml version="1.0" encoding="utf-8"?>\n')
fOut.write('<html>\n')
fOut.write('<body>\n')

for sent in sents:
    print (sent + ' SENT')
    fOut.write('<se>\n')
    fOut.write('<sent>' + sent + '</sent>\n')
    sent = sent.split()
    for i in sent:
        m = ''
        while len(i) > 0:
            if i not in words:
                m += i[-1]
                i = i[:-1]
            else:
                fOut.write('<w>')
                for word in china_dict:
                    if i == word[1]:
                        fOut.write('<ana lex="' + i + '" transcr="' + word[2] + '" sem="' + word[3] + '"/>')
                fOut.write(i + '</w>' + '\n')
                i = m[::-1]
                m = ''
    fOut.write('</se>\n')
fOut.write('</body>\n</html>')
fOut.close()