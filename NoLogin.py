__author__ = 'jincj'
#coding=utf-8

#参考网址
#http://blog.csdn.net/beiji_nanji/article/details/7487472
#http://cuiqingcai.com/990.html
#http://www.crifan.com/files/doc/docbook/web_scrape_emulate_login/release/html/web_scrape_emulate_login.html
#http://www.crifan.com/files/doc/docbook/web_scrape_emulate_login/release/html/web_scrape_emulate_login.html

import urllib.request
from bs4 import BeautifulSoup
import re

#存储文件
def saveFile(data, fileName):
    #save_Path = 'E:\\Python\\SaveFile\\'
    #save_Path += fileName
    print('将网页写入到文件：' + fileName)
    f_obj = open(fileName, 'wb')
    f_obj.write(data)
    f_obj.close()

class NoLoginRequest:
    def __init__(self,url,page):
        self._url = url
        self._page = page
        self._path = 'E:\\Python\\SaveFile\\'
        #self._header={
        #    'Connection': 'Keep-Alive',
        #    'Accept': 'text/html, application/xhtml+xml, */*',
        #    'Accept-Language': 'zh-CN',
        #    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #    'Accept-Encoding': 'gzip, deflate',
        #    'Host': 'www.qiushibaike.com/',
        #    'DNT': '1'
        #}
        self._header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',}



    def start(self):
        #for key,value in self._header.items():
            #print(key,':',value)

        try:
            for page in range(1,self._page+1):
                requestUrl = self._url + str(page)
                print('正在访问网页   ' + requestUrl)
                #req = urllib.request.Request(requestUrl, headers=self._header)
                #response = urllib.request.urlopen(req)
                #data = response.read()

                saveFileName = self._path + 'qiushibaike' + str(page) + '.html'
                print(saveFileName)
                #saveFile(data, saveFileName)
                #data = data.decode()

                strDataFile = open(saveFileName)
                strData = strDataFile.read()
                print(strData)
                #strData = strData.decode('UTF-8','ignore')
                #soup = BeautifulSoup(open(saveFileName))
                #soup = BeautifulSoup(strData)
                #print(soup.prettify())





                #pattern = re.compile('<div.*?class="author"><a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+
                                     #'="content">(.*?)', re.S)
                #pattern = re.compile('<div.*?class="author">.*?<a.*?<img.*?(.*?)</a>.*?</div>', re.S)
                #pattern = re.compile('<div.*?class="author">.*?<a.*?<img.*?/>.*?(.*?)</a>.*?</div>/*?<div.*?class="content">(.*?)</div>', re.S)
                #items = re.findall(pattern, data)
                #items = re.findall(pattern, '<div class="author"> <a href="/users/29365176" target="_blank"> <img src="http://pic.qiushibaike.com/system/avtnew/2936/29365176/medium/20150711113434.jpg" />磨头岩肥佬</a></div>')

                #for item in items:
                #    print(item)

        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('Error Reason',e.reason)
            elif hasattr(e, 'code'):
                print('Error Code:', e.code)
            else:
                print('Good!')




#
noLoginRequest = NoLoginRequest('http://www.qiushibaike.com/8hr/page/', 1)
noLoginRequest.start()


