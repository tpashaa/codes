# -*- coding: utf-8 -*-
"""
@author: Pasha
"""
import os, subprocess

def wikiextractor(wiki_dump, wiki_extractor= './WikiExtractor.py',result='./wiki_extracted/'):
    if not os.path.exists(result):
        os.makedirs(result)
    subprocess.call(['python',wiki_extractor,'-o',result,wiki_dump])

dump = 'ruwiki-20160407-pages-articles.xml'
wikiextractor(dump)
