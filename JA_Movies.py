# -*- coding:utf-8 -*-


import requests,SQL
from lxml import etree

class JA_Movies(object):
    def __init__(self,baseUrl,filePath):
        self.baseUrl = baseUrl
        self.pathDB = filePath + 'JA.db'
        self.session = requests.Session()
        self.cursor = SQL.SQL().cursor

        # http://www.j9lib.com/cn/vl_star.php?&mode=2&s=azabi  所有影片
        # http://www.j9lib.com/cn/vl_star.php?&mode=1&s=azabi  有评论的

    # 获取演员第一页电影
    def getDefaultPage(self,nameUrl):
        u1 = nameUrl.split('?')[0]
        u2 = nameUrl.split('?')[1]
        pageUrl = self.baseUrl + u1 + '?&mode=2&' +u2
        for i in xrange(10):
            try:
                # webPage = self.session.get(pageUrl,timeout = 30)
                webPage = self.session.get(pageUrl,timeout=20)
                return webPage
            except requests.exceptions.Timeout as te:
                print te
                pass
            except requests.exceptions.ConnectionError as e:
                print e
                pass



    # 获取最大页码
    def getMaxPageNumWithPrefix(self,webPage):
        selector = etree.HTML(webPage.text)
        maxPageNumList = selector.xpath(r'//*[@class="page_selector"]/a/@href')
        if len(maxPageNumList) > 0:
            lastNum = maxPageNumList[-1]
            maxPageNum = lastNum.split('=')[-1]
            return int(maxPageNum)
        else:return 1

    # 获取演员下面第1页第2页的url
    def getMoviePageFromPageNum(self,nameUrl,pageNum):
        u1 = nameUrl.split('?')[0]
        u2 = nameUrl.split('?')[1]
        print '第' + str(pageNum) + '页'
        pageUrl = self.baseUrl + u1 + '?&mode=2&' + u2 + '&page=' + str(pageNum)
        print pageUrl
        return pageUrl

    # 获取第x页面上的所有movieUrl
    def getMovieUrlFromPageUrl(self,pageUrl):
        for i in xrange(10):
            try:
                webPage = self.session.get(pageUrl,timeout=20)
                selector = etree.HTML(webPage.text)
                movieList = selector.xpath(r'//div/div/div/a/@href')
                movieUrls = set()
                for s in movieList:
                    movieUrls.add(s[1:])
                return movieUrls
            except requests.exceptions.Timeout as te:
                print te
                pass
            except requests.exceptions.ConnectionError as e:
                print e
                pass

