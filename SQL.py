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


    def insertNameAndNameURL(self,nameList,nameUrlList):
        for index in range(len(nameList)):
            name = nameList[index]
            nameUrl = nameUrlList[index]
            print name + ' : ' + nameUrl
            self.cursor.execute("INSERT INTO JA_NAME (NAME,NAME_URL) VALUES (?,?)",(name,nameUrl))
        self.conn.commit()
        print 'insert nameUrl sqlite suceess'

    def insertNameAndMovieURL(self,name,movieUrlList):
        for url in movieUrlList:
            self.cursor.execute("INSERT INTO JA_MOVIE_URL (NAME,MOVIE_URL) VALUES (?,?)",(name,url))
        self.conn.commit()
        print 'insert movieUrl sqlite suceess'



    def quaryMaxIndex(self):
        result = self.cursor.execute('SELECT count(*)  FROM JA_NAME ')
        maxIndex = result.fetchone()[0]
        print '共' + str(maxIndex) + '条'
        return maxIndex

    def quaryNameUrlFromDB(self,index):
        selectResult = self.cursor.execute('SELECT * FROM JA_NAME WHERE ID = ? ',(index,))
        result = selectResult.fetchone()
        nameUrl = result[1]
        name = result[2]
        return nameUrl,name
        # return 'vl_star.php?&mode=2&s=arevi'