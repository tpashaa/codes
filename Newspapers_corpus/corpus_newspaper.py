import os, requests, re, shutil
from bs4 import BeautifulSoup
url = u"http://mgazeta.com/"
linksfile = open(u'links.txt', 'w')

def getlink(url):
    news_links = []
    block_links = []
    page_nums = []
    r = requests.get(url)
    page = BeautifulSoup(r.text, "html.parser")
    blocks = page.find(id="topnav")("a")
    for block in blocks:
        m = re.search(u'(http://mgazeta.com/category/.*?/)', block['href'])
        if m != None:
            if m.group(0) not in block_links:
                block_links.append(m.group(0))
    for i in block_links:
        r = requests.get(i)
        page = BeautifulSoup(r.text, "html.parser")
        n = page.findAll("a", {"class": "page"})
        page_nums.append([i, n[-1].get("title")])
    for i in page_nums:
        print (u'URL --> ' + i[0])
        num = int(i[1])
        while num >= 0:
            print (u'собираем ссылки со страницы --> ' + str(num))
            r = requests.get(i[0] + u'/page/' + str(num))
            num -= 1
            page = BeautifulSoup(r.text, "html.parser")
            news = page.findAll("a", {"rel": "bookmark"})
            del news[-1]
            for n in news:
                if n['href'] not in news_links:
                    news_links.append(n['href'])
    return news_links
    
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
      
def error_links(links):
    mass = []
    for i in links:
        r = requests.get(i)
        page = BeautifulSoup(r.text, "html.parser")
        header = page.find("a", {"rel": "bookmark"})
        if header == None:
            print (u'найдена плохая ссылка --> ' + i)
            mass.append(i)
    return mass


all_links = getlink(url)
print (u'ищем плохие ссылки и удаляем их из основного списка')
error_links = error_links(all_links)

for i in error_links:
    all_links.remove(i)

n = 1
for i in all_links:
    linksfile.write(str(n) + u': ' + i + '\n')
    n += 1
linksfile.close()
    
n = 1
for i in all_links:
    print (u"записываем новость --> " + str(n) + ' ' + i)
    filefolder(i, n)
    n += 1