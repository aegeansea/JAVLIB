# -*- coding:utf-8 -*-

import sqlite3
class SQL(object):
    def __init__(self):
        self.conn = sqlite3.connect('/Users/mbp/Desktop/JA/JA.db')
        self.cursor = self.conn.cursor()

    def createTable(self):
        self.conn.execute('''CREATE TABLE JA_NAME
               (ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME           TEXT,
               NAME_URL       TEXT);''')
        print 'create table JA_NAME success'


    def createMovieUrlTable(self):
        self.conn.execute('''CREATE TABLE JA_MOVIE_URL
                       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       NAME           TEXT,
                       MOVIE_URL       TEXT);''')
        print 'create table JA_MOVIE_URL success'

    # 番号 ABP-525
    # //*[@id="video_id"]/table/tbody/tr/td[2]
    # 海报图片地址
    # //*[@id="video_jacket_img"]/@src
    # 评分 (9.4)
    # //*[@id="video_review"]/table/tbody/tr/td[2]/span[2]
    # 日期 2016-10-11
    # //*[@id="video_date"]/table/tbody/tr/td[2]
    # 影片时长
    # //*[@id="video_length"]/table/tbody/tr/td[2]
    # 演员
    # //span/span[1]/a
    # 影片类型
    # //*[@id="video_genres"]/table/tbody/tr/td[2]
    # 想要这个影片
    # //*[@id="subscribed"]/a
    # 看过这个影片
    # //*[@id="watched"]/a
    # 拥有这个影片
    # //*[@id="owned"]/a

    def createMovieInfoTable(self):
        self.conn.execute('''CREATE TABLE JA_MOVIE_INFO
                       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                       FH           TEXT,
                       IMAGE_URL    TEXT,
                       PF           TEXT,
                       DATE         TEXT,
                       SC           TEXT,
                       YY           TEXT,
                       TYPE         TEXT,
                       SUBSCRIBED   TEXT,
                       WATCHED      TEXT,
                       OWNED        TEXT);''')
        print 'create table JA_MOVIE_INFO success'


    def insertNameAndNameURL(self,nameList,nameUrlList):
        for index in range(len(nameList)):
            name = nameList[index]
            nameUrl = nameUrlList[index]
            print name + ' : ' + nameUrl
            self.cursor.execute("INSERT INTO JA_NAME (NAME,NAME_URL) VALUES (?,?)",(name,nameUrl))
        self.conn.commit()
        # print 'insert nameUrl sqlite suceess'


    def insertNameAndMovieURL(self,name,movieUrlList):
        for url in movieUrlList:
            self.cursor.execute("INSERT INTO JA_MOVIE_URL (NAME,MOVIE_URL) VALUES (?,?)",(name,url))
        self.conn.commit()
        # print 'insert movieUrl sqlite suceess'


    #查询演员数量
    def quaryMaxIndex(self):
        result = self.cursor.execute('SELECT count(*)  FROM JA_NAME ')
        maxIndex = result.fetchone()[0]
        print '共' + str(maxIndex) + '条'
        return maxIndex

    #根据ID找出演员URL
    def quaryNameUrlFromDB(self,index):
        selectResult = self.cursor.execute('SELECT * FROM JA_NAME WHERE ID = ? ',(index,))
        result = selectResult.fetchone()
        nameUrl = result[1]
        name = result[2]
        return nameUrl,name
        # return 'vl_star.php?&mode=2&s=arevi'

    #根据ID找出影片URL
    def quaryUrlFromIndex(self,index):
        selectResult = self.cursor.execute('SELECT * FROM JA_M_URL WHERE ID = ?',(index,))
        result = selectResult.fetchone()
        movieUrl = result[2]
        name = result[1]
        print str(index) + '   ' +name
        return movieUrl

    #保存影片信息
    def insertMovieInfo(self,info):
        # Info = (fanHao,riQi,changDU,daoYan,zhiZuoShang,faXingShang,pinFen,leiBie,yanYuanLieBiao,xiangYao,kanGuo,yongYOU)

        self.cursor.execute("INSERT INTO JA_NAME (NAME,NAME_URL) VALUES (?,?)", (name, nameUrl))



