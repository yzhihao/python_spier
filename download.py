__author__ = 'yzh'
#coding=utf-8
import urllib2
class htmldowmloader(object):
    def download(self,url):
        if url is None:
            return None
        try:
            response=urllib2.urlopen(url)
            if response.getcode()!= 200:
                return None
        except Exception, e:
            print('Exception='+str(e))

        return response.read()