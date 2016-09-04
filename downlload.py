from pip._vendor.requests.packages.urllib3 import response
#coding=utf-8
import urllib2
__author__ = 'yzh'
class htmldowmloader(object):
    def download(self,url):
        if url is None:
            return None

        response=urllib2.urlopen(url)
        if response.getcode()!= 200:
            return None
        return response.read()


