__author__ = 'yzh'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib2
from bs4 import BeautifulSoup
if __name__=="__main__":
    i=1
    while(1):
    	#here is the location of the PhantomJS
        browser = webdriver.PhantomJS("E:/phantomjs/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        browser.get('http://news.ifeng.com/a/20160909/49939696_0.shtml')
        # we can click it just as we ussally do by our browser
        browser.execute_script("document.getElementsByClassName('left_dz ipad_none iphone_none')[0].click()")
        print("this is num %d"%(i))
        html=browser.page_source
        soup=BeautifulSoup(html,'html.parser',from_encoding='utf-8')
        links=soup.find('div',class_='left_dz ipad_none iphone_none left_dz_hover').find('span')
        print('the thank is '+str(links.get_text()))
        i+=1
        if(i>30):
            break

    # for link in  links:
    #     new_url=link['title']
    #     print(new_url)
# a class="js-expand zg-right zg-gray-normal" href="#">
# then
#ActionChains(driver).click(driver.find_element_by_id('func46')).perform()

