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

class NoLoginRequest:
    def __init__(self,url,page):
        self._url = url
        self._page = page
        self._path = 'E:\\Python\\SaveFile\\qiushibaike'
        self._file = self._path + str(self._page) + '.html'
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

    #存储文件
    def saveFile(self, data, requestUrl, page):
        self._file = self._path + page + '.html'
        print('将网页:' + requestUrl + ' 写到文件：' + self._file)
        f_obj = open(self._file, 'wb')
        f_obj.write(data)
        f_obj.close()

    def getPageData(self):
        requestUrl = self._url + str(page)
        print('正在访问网页   ' + requestUrl)
        req = urllib.request.Request(requestUrl, headers=self._header)
        response = urllib.request.urlopen(req)
        data = response.read().decode('UTF-8')

    def start(self):
        try:
            for page in range(1,self._page+1):

                #print(data)
                #self.saveFile(data, requestUrl, str(page))

                #data = data.decode('unicode-escape')
                #data = data.decode('UTF-8','ignore')
                #encodeData = data.encode('GBK','ignore')
                #encodeData = data.encode('GB18030')
                #print('打开文件名：' + self._file)
                #openFile = open(self._file, 'r')
                #openData = openFile.read().encode('GBK')
                #openFile.close()

                #print(openData.encode('gbk','ignore'))
                #print(openData.encode('gbk','ignore'))

                #saveFileName = self._path + 'qiushibaike' + str(page) + '.html'
                #print(saveFileName)
                #self.saveFile(data, str(page))
                #data = data.decode()

                #.*?<span.*?"dash">.*?<i.*?class="number">(.*?)</i>
                #.*?<div.*?class="stats">.*?<span.*?"status">.*?<i.*?class="number">(.*?)</i>.*?</span>
                #.*?<div.*?class="stats">.*?<i.*?class="number">(.*?)</i>.*?</span>
                #.*?<span.*?"dash">.*?<i.*?class="number">(.*?)</i>.*?</span>
                #.*?<div.*?class="thumb">.*?<img.*?"(.*?".*?/>.*?</div>
                #.*?<div.*?class="stats">.*?<i.*?class="number">(.*?)</i>.*?</span>.*?<span.*?"dash">.*?<i.*?class="number">(.*?)</i>.*?</span>

                pattern = re.compile('<div.*?class="author">.*?<img.*?/>(.*?)</a>.*?</div>.*?<div.*?class="content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div.*?class="stats">.*?<i.*?class="number">(.*?)</i>.*?</span>.*?<span.*?"dash">.*?<i.*?class="number">(.*?)</i>.*?</span>', re.S)
                #pattern = re.compile('<div.*?class="thumb">.*?<a.*?<img.*?src="(.*?)".*?/>.*?</div>', re.S)
                items = re.findall(pattern, data)

                for item in items:
                    havingImg = re.search("img",item[3])
                    print(item)
                    #if not havingImg:
                    #    print(item[0],item[1],item[2],item[4],item[5])


        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('Error Reason',e.reason)
            elif hasattr(e, 'code'):
                print('Error Code:', e.code)
            else:
                print('Good!')





noLoginRequest = NoLoginRequest('http://www.qiushibaike.com/8hr/page/', 1)
noLoginRequest.start()


