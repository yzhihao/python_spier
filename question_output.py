#coding=utf-8
__author__ = 'yzh'

import dbutil
import url

class sqloutput(object):
    def __init__(self):
        self.date=[]
        self.db=dbutil.dbutil()
        self.count=url.url()

    def collect(self,date):
        if date is None:
            return
        self.save_date(date)

    def save_date(self,date):
        try:
            a=date['attention'].encode('utf-8')
            a1=a.split('\n')
            date['attention']=a1[3]

            c=date['comment'].encode('utf-8')
            if(c=='\n添加评论\n'):
                date['comment']=0
            else:
                c1=c.split('\n')
                c2=c1[1]
                c3=c2.split(' 条评论')
                date['comment']=c3[0]
        except  Exception, e:
            print('convert_Exception='+str(e))
            exit()
        count=self.count.count_('question',date['url'])
        if count==0:
            conn,cursor=self.db.getcon()
            try:
                cursor.execute('insert into question (name,comment,tags,answer_num,question_url,attention) values (%s,%s,%s,%s,%s,%s);',
                               [date['name'],date['comment'],date['tags'],date['answer_num'],date['url'],date['attention']])
            except  Exception, e:
               print('Exception='+str(e))
            self.db.closecon(conn,cursor)
