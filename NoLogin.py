__author__ = 'jincj'
#coding=utf-8

#参考网址
#http://blog.csdn.net/beiji_nanji/article/details/7487472
#http://cuiqingcai.com/990.html

import urllib.request

class NoLoginRequest:
    def __init__(self,url,page):
        self._url = url
        self._page = page
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
                print('正在访问网页   '+requestUrl)
                #req = urllib.request.Request(requestUrl, headers=self._header)
                #response = urllib.request.urlopen(req)
                #data = response.read().decode()
                #print(data)

        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('Error Reason',e.reason)
            elif hasattr(e, 'code'):
                print('Error Code:', e.code)
            else:
                print('Good!')





#http://www.qiushibaike.com/8hr/page/2?s=4791266
noLoginRequest = NoLoginRequest('http://www.qiushibaike.com/8hr/page/', 5)
noLoginRequest.start()


