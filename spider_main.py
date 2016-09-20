#coding=utf-8
__author__ = 'yzh'

import url
import people_output
import question_output
import parser_
import download
import question_parser
import time

class  spidermain():
    def __init__(self):
        self.o_urls=url.url()
        self.o_download=download.htmldowmloader()
        self.output=people_output.sqloutput()
        self.question_output=question_output.sqloutput()
        self.parser=parser_.parse1()
        self.question_parser=question_parser.question_parser()

    def spiderquestionmain(self,count):
        count_=count
        errorcount=1
        while self.o_urls.isquestionempty():
            try:
                new_uel=self.o_urls.get_newquestion_url(count)
                print(u'这是第%d个问题网页，地址是:%s'%(count,new_uel))
                print(u'问题集合中还剩%d个url'%(self.o_urls.getquestionurlnum()))
                html_cont=self.o_download.download(new_uel)
                print('download is ok')
                time.sleep(2)
                new_uels,new_date=self.question_parser.parser(new_uel,html_cont)
                print('parser is ok')
                self.o_urls.addpeople_urls(new_uels)
                self.question_output.collect(new_date)
                print('question_output is ok')
                count=count+1
                if count==count_+10000:
                    break
                errorcount=1
            except:
                errorcount+=1
                count=count+1
                print (u"spiderquestionmain-此地址无效")
            if(errorcount>=10):
                exit()
        return count

    def spiderpeoplemain(self,fristurl):
        count=119486
        question_count=56441
        errorcount=1
        # self.o_urls.addpeople_url(fristurl)
        # self.o_urls.addquestion_url('https://www.zhihu.com/question/50136311')
        while self.o_urls.isquestionempty():
            count_=count
            while self.o_urls.ispeopleempty():
                try:
                    new_uel=self.o_urls.get_newpeople_url(count)
                    print(u'这是第%d个用户网页，地址是:%s'%(count,new_uel))
                    print(u'用户集合中还剩%d个url'%(self.o_urls.getpeopleurlnum()))
                    html_cont=self.o_download.download(new_uel)
                    print('download is ok')
                    # time.sleep(1)
                    new_uels,new_date=self.parser.parser(new_uel,html_cont)
                    print('parser is ok')
                    self.o_urls.addquestion_urls(new_uels)
                    self.output.collect(new_date)
                    print('output is ok')
                    count=count+1
                    if count==count_+10000:
                        break
                    errorcount=1
                except:
                    errorcount+=1
                    count=count+1
                    print (u"此地址无效")
                if(errorcount>=10):
                    exit()

            question_count=self.spiderquestionmain(question_count)


if __name__=="__main__":
    fristurl="https://www.zhihu.com/people/excited-vczh"
    O_Spidermain=spidermain()
    O_Spidermain.spiderpeoplemain(fristurl)