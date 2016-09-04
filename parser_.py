# -*-coding:gbk-*-
import urlparse
import re
from bs4 import BeautifulSoup

__author__ = 'yzh'


class parse1(object):
    def __init__(self):
        pass

    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        for link in  links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return  new_urls

#<h1>Python</h1><dd class="lemmaWgt-lemmaTitle-title">
#<table id="Table1" class="blacktab" bordercolor="Black" border="0" width="100%">
    #<tr class="trbg1">
    def _get_new_date(self,page_url,soup):
        res_date={}
        res_date['url']=page_url
        tilte_node=soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find("h1")
        res_date['tittle']=tilte_node

        summy_node=soup.find('div',class_="lemma-summary")
        res_date['summy']=summy_node
        return  res_date

    def parser(self,page_url,html_cont):
        if page_url is None or  html_cont is None:
            return

        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        newdate=self._get_new_date(page_url,soup)
        return new_urls,newdate