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
        imageUrl = info[0]
        fanHao = info[1]
        riQi = info[2]
        changDu = info[3]
        daoYan = info[4]
        zhiZuoShang = info[5]
        faXingShang = info[6]
        pinFen = info[7]
        leiBie = info[8]
        yanYuanLieBiao = info[9]
        xiangYao = info[10]
        kanGuo = info[11]
        yongYou = info [12]
        self.cursor.execute("INSERT INTO JA_MOVIE_INFO (IMAGE_URL,FANHAO,RIQI,CHANGDU,DAOYAN,ZHIZUOSHANG,FAXINGSHANG,PINFEN,LEIBIE,YANYUANLIEBIAO,XIANGYAO,KANGUO,YONGYOU) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(imageUrl,fanHao,riQi,changDu,daoYan,zhiZuoShang,faXingShang,pinFen,leiBie,yanYuanLieBiao,xiangYao,kanGuo,yongYou))
        self.conn.commit()
        # print 'insert movie_info sqlite suceess'








