# -*- coding:utf-8 -*-


import SQL,JA_Name,JA_Movies,JA_Info
import requests
# from lxml import etree

class SpiderJAV:
    def __init__(self,baseUrl,filePath):
        self.baseUrl = baseUrl
        self.filePath = filePath
        self.ja_name = JA_Name.JA_Name(baseUrl)
        self.sql = SQL.SQL()
        self.ja_movies = JA_Movies.JA_Movies(baseUrl,filePath)
        self.ja_info = JA_Info.JA_Info(baseUrl)


    def getNamesFromJavLib(self):
        try:
            # 首次执行如果没有建表就创建表格
            self.sql.createTable()
        except:
            preFix = self.ja_name.getAllPreFix()
            for char in preFix:
                print char
                page = self.ja_name.getPreFixPage(char)
                maxNum = self.ja_name.getMaxPageNumWithPrefix(page)
                index = 1
                while index <= int(maxNum):
                    url = self.ja_name.getWebPage(char, index)
                    index += 1
                    (nameUrlList, nameList) = self.ja_name.getAllNameFromPageUrl(url)
                    self.sql.insertNameAndNameURL(nameUrlList, nameList)


    # def getMoviesWithName(self):
    # http://www.j9lib.com/cn/vl_star.php?&mode=2&s=ayote
    def getFanHaoUrl(self):
        try:
            # 首次执行如果没有建表就创建表格
            self.sql.createMovieUrlTable()
        except:
            maxIndex = self.sql.quaryMaxIndex()
            for index in xrange(36317,37799):
                # 数据库中ID为 1-37798,如果断了就改下for循环启示标志位,从这一位演员开始
                (nameUrl,name) = self.sql.quaryNameUrlFromDB(index + 1)
                defPage = self.ja_movies.getDefaultPage(nameUrl)  #第一页
                maxNum = self.ja_movies.getMaxPageNumWithPrefix(defPage) #获取最大页码
                print str(index) + '  ' +  name
                print '页数' + str(maxNum)
                maxNum += 1
                for pageIndex in xrange(1,maxNum):
                    moviePageUrl = self.ja_movies.getMoviePageFromPageNum(nameUrl,pageIndex)
                    movieUrls = self.ja_movies.getMovieUrlFromPageUrl(moviePageUrl)
                    self.sql.insertNameAndMovieURL(name,movieUrls)

    def getMovieInfo(self,fromIndex,toIndex):
        for index in xrange(fromIndex,toIndex):
            urlName = self.sql.quaryUrlFromIndex(index)
            name = urlName[1]
            url = urlName[0]
            page = self.ja_info.getMoviePageFromUrl(url)
            result = self.ja_info.getInfoFromMoviePage(page)
            self.sql.insertMovieInfo(result,name)


# http://www.j9lib.com/cn/vl_star.php?&mode=&s=azccm&page=1
base = 'http://www.javl10.com/cn'
filePath = '/Users/mbp/Desktop/JA/'
spider = SpiderJAV(base,filePath)
# nameUrl = spider.sql.quaryNameUrlFromDB(1)
# spider.getNamesFromJavLib()
# spider.getFanHaoUrl()

spider.getMovieInfo(70412,80000)



# spider.ja_name.getAllPreFix()
# page = spider.ja_info.getMoviePageFromUrl('?v=javlii3j34')
# result = spider.ja_info.getInfoFromMoviePage(page)
# spider.sql.insertMovieInfo(result)

