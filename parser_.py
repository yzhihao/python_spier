# -*-coding:UTF-8-*-
import urlparse
import re
from bs4 import BeautifulSoup

__author__ = 'yzh'


class parse1(object):
    def __init__(self):
        pass

    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'/question/.+'))
        for link in  links:
            new_url=link['href']
            a=new_url.split('/answer')
            new_url=a[0]
            new_full_url=urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return  new_urls


    def _get_new_date(self,page_url,soup):
        res_date={}
        res_date['url']=page_url
        try:
            tilte_node=soup.find('div',class_='title-section').find("span")
            res_date['name']=tilte_node.get_text()
        except:
                res_date['name']='NULL'

        try:
            amg=soup.find('img',class_="Avatar Avatar--l")
            res_date['amg']=amg["src"]
        except:
            res_date['amg']='NULL'

        try:
            attention=soup.find('a',href=re.compile(r'/people/.+/followers')).find('strong')
            res_date['attention']=attention.get_text()
        except:
            res_date['attention']='NULL'

        # 这里为了抛出错误，当ip限制时抛出
        answer_num=soup.find('a',href=re.compile(r'^/people/.+/answers$')).find('span')
        res_date['answer_num']=answer_num.get_text()


        try:
            question_num=soup.find('a',href=re.compile(r'^/people/.+/asks$')).find('span')
            res_date['question_num']=question_num.get_text()
        except:
            res_date['question_num']='NULL'

        try:
            article=soup.find('a',href=re.compile(r'^/people/.+/posts$')).find('span')
            res_date['article']=article.get_text()
        except:
            res_date['article']='NULL'

        try:
            collections=soup.find('a',href=re.compile(r'^/people/.+/collections$')).find('span')
            res_date['collections']=collections.get_text()
        except:
         res_date['collections']='NULL'

        try:
            location=soup.find('span',class_="location item")
            res_date['location']=location["title"]
        except:
            res_date['location']='NULL'

        try:
            business=soup.find('span',class_="business item")
            res_date['business']=business["title"]
        except:
            res_date['business']='NULL'

        try:
            employment=soup.find('span',class_="employment item")
            res_date['employment']=employment["title"]
        except:
            res_date['employment']='NULL'

        try:
            position=soup.find('span',class_="position item")
            res_date['position']=position["title"]
        except:
            res_date['position']='NULL'

        try:
            education=soup.find('span',class_="education item")
            res_date['education']=education["title"]
        except:
            res_date['education']='NULL'

        try:
            education_extra=soup.find('span',class_="education-extra item").find("a")
            res_date['education_extra']=education_extra["title"]
        except:
            res_date['education_extra']='NULL'

        try:
            agreement=soup.find('span',class_="zm-profile-header-user-agree").find("strong")
            res_date['agreement']=agreement.get_text()
        except:
            res_date['agreement']='NULL'

        try:
            thanks=soup.find('span',class_="zm-profile-header-user-thanks").find("strong")
            res_date['thanks']=thanks.get_text()
        except:
            res_date['thanks']='NULL'

        try:
            topics=soup.find('div',class_='zm-profile-side-topics').find_all('img',class_='Avatar Avatar--l')
            topic_=''
            for topic in  topics:
                new_topic=topic["alt"]
                topic_=topic_+'+'+new_topic
            res_date['topic']=topic_
        except  Exception, e:
            print('Exception='+str(e))
            res_date['topic']='NULL'


        return  res_date

    def parser(self,page_url,html_cont):
        if page_url is None or  html_cont is None:
            return

        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        newdate=self._get_new_date(page_url,soup)
        return new_urls,newdate