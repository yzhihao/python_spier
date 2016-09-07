__author__ = 'yzh'
import urlparse
import re
from bs4 import BeautifulSoup
class question_parser():
    def __init__(self):
        pass

    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find_all('a',class_='author-link',href=re.compile(r'/people/.+'))
        for link in  links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return  new_urls


    def _get_new_date(self,page_url,soup):
        res_date={}
        res_date['url']=page_url
        try:
            tilte_node=soup.find('span',class_='zm-editable-content')
            res_date['name']=tilte_node.get_text()
        except:
                res_date['name']='NULL'

        try:
            comment=soup.find('a',class_="toggle-comment meta-item")
            res_date['comment']=comment.get_text()
        except:
            res_date['comment']='NULL'

        try:
            tags=soup.find_all('a',class_='zm-item-tag')
            tag_=''
            for tag in  tags:
                new_tag=tag.get_text()
                tag_=tag_+'+'+new_tag
            res_date['tags']=tag_
        except  Exception, e:
            print('Exception='+str(e))
            res_date['tags']='NULL'


        try:
            answer_num=soup.find('h3',id="zh-question-answer-num")
            res_date['answer_num']=answer_num['data-num']
        except:
            res_date['answer_num']='NULL'


        try:
            attention=soup.find('div',class_="zm-side-section-inner zg-gray-normal")
            res_date['attention']=attention.get_text()
        except Exception, e:
            print('Exception='+str(e))
            res_date['attention']='NULL'

        return  res_date

    def parser(self,page_url,html_cont):
        if page_url is None or  html_cont is None:
            return

        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        newdate=self._get_new_date(page_url,soup)
        return new_urls,newdate