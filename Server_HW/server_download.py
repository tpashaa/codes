import os, requests, re, shutil, codecs
from bs4 import BeautifulSoup
url = u"http://mgazeta.com/"
    
def filefolder(url, num):
    r = requests.get(url)
    page = BeautifulSoup(r.text, "html.parser")
    header = page.find("a", {"rel": "bookmark"}).text
    header = str(n) + u' ' + header

    
    date = page.find("span", {"class": "date"}).text
    m = re.search(u"[0-9]+.([0-9]+).([0-9]+).*", date)
    if m != None:
        month = m.group(1)
        year = m.group(2)
        
    file = open(header + '.txt','w', encoding='utf-8')
    file.write('@ti ' + header + '\n')
    file.write('@da ' + date + '\n')
    file.write('@url ' + url + '\n' + '\n')
    
    text = page.findAll("p", style="text-align: justify;")
    if text == []:
        file.write(u'Скачивание данной статьи ещё в разработке')
    else:
        for i in text:
            file.write(i.text + '\r\n')
    
    if not os.path.exists(year):
        os.makedirs(year)
    if not os.path.exists(year + '\\' + month):
        os.makedirs(year + '\\' + month)
    if not os.path.exists(year + '\\' + month):
        os.makedirs(year + '\\' + month)
    if not os.path.exists(year + '\\' + month + '\\' + header + '.txt'):
        shutil.move(header + '.txt', year + '\\' + month)
    else:
        os.remove(header + '.txt')

def read_links(file):
    links = []
    fIn = codecs.open(file, 'r', 'utf-8')
    for line in fIn:
        m = re.search('.*?: (http://mgazeta.com/.*?html)', line)
        if m != None:
            links.append(m.group(1))
    return links

all_links = read_links('links.txt')

print (all_links[0:10])
n = 1
for i in all_links[0:10]:
    print (u"записываем новость --> " + str(n) + ' ' + i)
    filefolder(i, n)
    n += 1