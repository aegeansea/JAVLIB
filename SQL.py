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
        print '建表成功'

    def insertNameAndNameURL(self,nameList,nameUrlList):
        for index in range(len(nameList)):
            name = nameList[index]
            nameUrl = nameUrlList[index]
            print name + ' : ' + nameUrl
            self.cursor.execute("INSERT INTO JA_NAME (NAME,NAME_URL) VALUES (?,?)",(name,nameUrl))
        self.conn.commit()
        print 'insert sqlite suceess'