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

        #self._user_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        self._header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',}


    def start(self):
        for key,value in self._header.items():
            print(key,':',value)

        try:
            req = urllib.request.Request(self._url, headers=self._header)
            #req.add_header(self._header)
            response = urllib.request.urlopen(req)
            data = response.read()
            print(data)
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                print('Error Reason',e.reason)
            elif hasattr(e, 'code'):
                print('Error Code:', e.code)
            else:
                print('Good!')






noLoginRequest = NoLoginRequest('http://www.qiushibaike.com/', 5)
noLoginRequest.start()


