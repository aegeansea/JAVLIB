# -*- coding:utf-8 -*-

import requests
from lxml import etree
from bs4 import BeautifulSoup

class JA_Info(object):
    def __init__(self,bUrl):
        self.baseUrl = bUrl
        self.session = requests.Session()


    def getMoviePageFromUrl(self,url):
        pageUrl = self.baseUrl + url
        print pageUrl
        for i in xrange(5):
            try:
                webPage = self.session.get(pageUrl, timeout=10)
                # print webPage.text
                return webPage.text
            except requests.exceptions.Timeout as te:
                print te
                pass
            except requests.exceptions.ConnectionError as e:
                print e
                pass





    def getInfoFromMoviePage(self,mPage):
        soup = BeautifulSoup(mPage,"html.parser")

        HB = soup.select('img[id="video_jacket_img"]')[0]
        imageUrl = HB['src']
        # print '海报' + ' '  + str(imageUrl)

        SBM = soup.select('div[id="video_id"]')[0].text
        FH = SBM.split(':')
        fanHao = str(FH[1]).strip()
        # print '番号' + ' ' + fanHao
        RQ = soup.select('div[id="video_date"]')[0].text
        riQi = str(RQ.split(':')[1]).strip()
        # print '发行日期' + ' ' + riQi
        CD = soup.select('div[id="video_length"]')[0].text
        changDU = CD.split(':')[1].strip()
        # print  changDU
        DY = soup.select('div[id="video_director"]')[0].text
        daoYan = DY.split(':')[1].strip()
        # print daoYan
        ZZS = soup.select('div[id="video_maker"]')[0].text
        zhiZuoShang = ZZS.split(':')[1].strip()
        # print zhiZuoShang
        FXS = soup.select('div[id="video_label"]')[0].text
        faXingShang = FXS.split(':')[1].strip()
        # print faXingShang
        PJ = soup.select('span[class="score"]')[0].text
        pinFen = PJ[1:4]
        # print pinFen
        LB = soup.select('div[id="video_genres"]')[0].text
        leiBie = LB.split(':')[1].strip()
        # print leiBie
        YY = soup.select('div[id="video_cast"]')[0].text
        yanYuanLieBiao = YY.split(':')[1].strip()
        # print yanYuanLieBiao
        SUBSCRIBED = soup.select('span[id="subscribed"]')[0].text
        xiangYao = SUBSCRIBED.split('(')[1].split(' ')[0]
        # print xiangYao
        WATCHED = soup.select('span[id="watched"]')[0].text
        kanGuo = WATCHED.split('(')[1].split(' ')[0]
        # print kanGuo
        OWNED = soup.select('span[id="owned"]')[0].text
        yongYOU = OWNED.split('(')[1].split(' ')[0]
        # print yongYOU
        Info = (imageUrl,fanHao,riQi,changDU,daoYan,zhiZuoShang,faXingShang,pinFen,leiBie,yanYuanLieBiao,xiangYao,kanGuo,yongYOU)
        return Info
