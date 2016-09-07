__author__ = 'yzh'
import dbutil

class url():
    def __init__(self):
        self.db=dbutil.dbutil()

    def count(self,table_name):
        count=1
        try:
            conn,cursor=self.db.getcon()
            if(table_name=='people_urls'):
                cursor.execute('select count(*) from (select url from people_urls where is_old=0)a;')
            elif(table_name=='question_urls'):
                cursor.execute('select count(*) from (select url from question_urls where is_old=0)a;')
            count = cursor.fetchall()[0][0]
            self.db.closecon(conn,cursor)
        except Exception, e:
           print('count-Exception='+str(e))
        return count

    def count_(self,table_name,url):
        count=1
        try:
            conn,cursor=self.db.getcon()
            if(table_name=='question'):
                cursor.execute('select count(*) from (select question_url from question where question_url=%s)a;',[url])
            elif(table_name=='user'):
                cursor.execute('select count(*) from (select userurl from user where userurl=%s)a;',[url])
            count = cursor.fetchall()[0][0]
            self.db.closecon(conn,cursor)
        except Exception, e:
           print('count__-Exception='+str(e))
        return count


    def judge(self,table_name,url):
        try:
            count=1
            conn,cursor=self.db.getcon()
            if(table_name=='people_urls'):
                cursor.execute('select count(*) from (select id from people_urls where url=%s)a;',[url])
            else:
                cursor.execute('select count(*) from (select id from question_urls where url=%s)a;',[url])
            count = cursor.fetchall()[0][0]
            self.db.closecon(conn,cursor)
        except Exception, e:
           print('judge-Exception='+str(e))
        return count

    def insert(self,table_name,url):
        try:
            conn,cursor=self.db.getcon()
            if(table_name=='people_urls'):
                cursor.execute('insert people_urls (url,is_old) values (%s,0);',[url])
            else:
                cursor.execute('insert question_urls (url,is_old) values (%s,0);',[url])
            self.db.closecon(conn,cursor)
        except Exception, e:
           print('insert-Exception='+str(e))


    def get_newpeople_url(self,curpeopleid):
        try:
            conn,cursor=self.db.getcon()
            cursor.execute('select url from people_urls where id=%d;'%(curpeopleid))
            newpeople_url = str(cursor.fetchall()[0][0])
            cursor.execute('update  people_urls set is_old=1 where id=%d;'%(curpeopleid))
            self.db.closecon(conn,cursor)
        except Exception, e:
           print('Exception='+str(e))
        return  newpeople_url

    def ispeopleempty(self):
        count=self.count('people_urls')
        return count!=0

    def getpeopleurlnum(self):
        count=self.count('people_urls')
        return count

    def addpeople_url(self,url):
        if url is None:
            return
        count=1
        count=self.judge('people_urls',url)
        if count==0:
            self.insert('people_urls',url)

    def addpeople_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            count=self.judge('people_urls',url)
            if count==0:
                self.insert('people_urls',url)

    def getquestionurlnum(self):
        count=self.count('question_urls')
        return count

    def get_newquestion_url(self,curquestionid):
        try:
            conn,cursor=self.db.getcon()
            curquestionid=curquestionid
            cursor.execute('select url from question_urls where id=%d;'%(curquestionid))
            newquestion_url = (cursor.fetchall()[0][0])
            cursor.execute('update  question_urls set is_old=1 where id=%d;'%(curquestionid))
            self.db.closecon(conn,cursor)
        except Exception, e:
            print('Exception='+str(e))
        return  newquestion_url

    def isquestionempty(self):
        count=self.count('question_urls')
        return count!=0

    def addquestion_url(self,url):
        if url is None:
            return
        count=self.judge('question_urls',url)
        if count==0:
            self.insert('question_urls',url)

    def addquestion_urls(self,urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            count=self.judge('question_urls',url)
            if count==0:
                self.insert('question_urls',url)



