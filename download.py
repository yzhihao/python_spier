__author__ = 'yzh'
#coding=utf-8
import urllib2
class htmldowmloader(object):
    def download(self,url):
        if url is None:
            return None
        try:
            proxy = urllib2.ProxyHandler({'http': '127.0.0.1:80 87'})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            response=urllib2.urlopen(url,timeout=5)
            if response.getcode()!= 200:
                return None
            print('response.urlopen is ok')
        except Exception, e:
            print('Exception='+str(e))
        try:
            html=response.read()
        except Exception, e:
            print('Exception='+str(e))
        return html