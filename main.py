# -*- coding:utf-8 -*-


import SQL,JA_Name
import requests
from lxml import etree

class SpiderJAV:
    def __init__(self,baseUrl,filePath):
        self.baseUrl = baseUrl
        self.filePath = filePath
        self.ja_name = JA_Name.JA_Name(baseUrl)
        self.sql = SQL.SQL()



    def getMovieListFromName(self,nameUrl):
        pageURL = self.baseUrl + nameUrl
        # print pageURL
        try:
            webPage = self.session.get(pageURL,timeout = 180)
            selector = etree.HTML(webPage.text)
            movieUrlList = selector.xpath(r'//div/div[*]/div/div/div/a/@href') #影片url
            # movieNameList = selector.xpath('//div/div/div/a/@title') #影片名字
            # print webPage.status_code
            return movieUrlList
        except requests.exceptions.RequestException as e:
            print e


# http://www.j9lib.com/cn/vl_star.php?&mode=&s=azccm&page=1

base = 'http://www.j9lib.com/cn/'
filePath = '/Users/mbp/Desktop/JA'
spider = SpiderJAV(base,filePath)
preFix = spider.ja_name.getAllPreFix()
try:
    spider.sql.createTable()
except:
    for char in preFix:
        print char
        page = spider.ja_name.getPreFixPage(char)
        maxNum = spider.ja_name.getMaxPageNumWithPrefix(page)
        index = 1
        while index <= int(maxNum):
            url = spider.ja_name.getWebPage(char, index)
            index += 1
            (nameUrlList, nameList) = spider.ja_name.getAllNameFromPageUrl(url)
            spider.sql.insertNameAndNameURL(nameUrlList, nameList)
















# nameYZ = spider.ja_name.getAllNameFromPage('A')
# nameUrlList = nameYZ[0]
# nameList = nameYZ[1]

# for index in range(len(nameUrlList)):
#     nameUrl = nameUrlList[index].split('?')[1]
#     name = nameList[index].text
#     print nameList[index].text + ' : ' + nameUrl
#     spider.sql.insertNameAndNameURL(name,nameUrl)

# for nameUrl in nameUrlList:
#     name = nameUrl.split('?')[1]
#     print '演员' + name
#     pageIndex = 2
#     n = 'vl_star.php?&mode=&' + name + '&page=' + str(pageIndex)
#     movieUrlList = spider.getMovieListFromName(n)
#     if len(movieUrlList) >0 :
#         print movieUrlList
