#coding=utf-8
import url
import output
import parser_
import downlload
__author__ = 'yzh'


class Spidermain(object):
    def __init__(self):
        self.o_urls=url.url()
        self.o_download=downlload.htmldowmloader()
        self.output=output.htmloutput()
        self.parser=parser_.parse1()

    def gospeder(self,fristurl):
        count=1
        self.o_urls._add_url(fristurl)
        while self.o_urls.isempty():
            try:
                new_uel=self.o_urls._get_new_url()
                print(u'这是第%d个网页，地址是:%s'%(count,new_uel))
                html_cont=self.o_download.download(new_uel)
                new_uels,new_date=self.parser.parser(new_uel,html_cont)
                self.o_urls._add_urls(new_uels)
                self.output.collect(new_date)
                count=count+1
                if count==1000 :
                    break
            except:
                print (u"此地址无效")
        self.output.output()


if __name__=="__main__":
    fristurl="http://baike.baidu.com/view/21087.htm"
    O_Spidermain=Spidermain()
    O_Spidermain.gospeder(fristurl)
