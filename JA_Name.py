# -*- coding:utf-8 -*-


import requests
from lxml import etree

# 名字根据首字母排列
# 每个首字母下面有多页

class JA_Name(object):
    def __init__(self,baseUrl):
        self.baseUrl = baseUrl
        self.session = requests.Session()
    # 获取所有首字母 A-Z
    def getAllPreFix(self):
        prefixUrl = 'http://www.j9lib.com/cn/star_list.php?prefix=A'
        webPage = self.session.get(prefixUrl)
        selector = etree.HTML(webPage.text)
        preFixList = selector.xpath(r'//*[@id="rightcolumn"]/div[2]/a')
        # print preFixList
        preFixListText = ['A']
        for name in preFixList:
            preFixListText.append(name.text)
        return preFixListText

    # 获得该首字母下的默认页面
    def getPreFixPage(self,prefix):
        allNamesUrl = self.baseUrl + 'star_list.php?prefix=' + prefix
        try:
            webPage = self.session.get(allNamesUrl,timeout = 60)
            return webPage
        except requests.exceptions.Timeout as e:
            print e
        except requests.exceptions.RequestException as e:
            print e

    #获得首字母下页面的最大页码
    def getMaxPageNumWithPrefix(self,webPage):
        selector = etree.HTML(webPage.text)
        maxPageNumList = selector.xpath(r'//*[@class="page_selector"]/a/@href')
        if len(maxPageNumList) > 0:
            lastNum = maxPageNumList[-1]
            maxPageNum = lastNum.split('=')[-1]
            return maxPageNum
        else:return 1

        # 获得首字母下页面的所有名字
    def getWebPage(self,preFix,index):
        pageUrl = self.baseUrl + 'star_list.php?prefix=' + preFix + '&page=' + str(index)
        print pageUrl
        return pageUrl

    def getAllNameFromPageUrl(self, Url):
        for index in xrange(10):
            try:
                webPage = requests.get(Url, timeout=60)
                selector = etree.HTML(webPage.text)
                nameUrlList = selector.xpath(r'//div/div/div/div/a/@href')  # 演员url
                nameListTemp = selector.xpath(r'//div/div/div/div/a')  # 演员名字
                # print webPage.status_code
                nameList = []
                for name in nameListTemp:
                    nameList.append(name.text)
                return (nameUrlList, nameList)
            except requests.exceptions.Timeout as e:
                print e