__author__ = 'yzh'
#coding=utf-8

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
        count=self.count.count_('user',date['url'])
        if count==0:
            conn,cursor=self.db.getcon()
            try:
                cursor.execute('insert into user (name,location,business,employment,position_,eduction,eduction_extra,agreement,'
                               'thank,userurl,amg,attention,answer_num,question_num,article,collections,topic)'
                               ' values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
                               [date['name'],date['location'],date['business'],date['employment'],date['position'],date['education'],
                                date['education_extra'],date['agreement'],date['thanks'],date['url'],date['amg'],date['attention'],date['answer_num'],
                                date['question_num'],date['article'],date['collections'],date['topic']
                                ])
            except  Exception, e:
               print('Exception='+str(e))
            self.db.closecon(conn,cursor)
