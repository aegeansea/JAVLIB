# -*- coding:utf-8 -*-

import requests
from lxml import etree

class JA_Info(object):
    def __init__(self,bUrl):
        self.baseUrl = bUrl
        self.session = requests.Session()


    def getMoviePageFromUrl(self,url):
        pageUrl = self.baseUrl + url
        for i in xrange(10):
            try:
                webPage = self.session.get(pageUrl, timeout=10)
                return webPage
            except requests.exceptions.Timeout as te:
                print te
                pass
            except requests.exceptions.ConnectionError as e:
                print e
                pass

    def getInfoFromMoviePage(self,mPage):
        selector = etree.HTML(mPage.text)
        fanHao = selector.xpath(r'//*[@id="video_id"]/table/tbody/tr/td[2]')
        haiBao = selector.xpath(r'//*[@id="video_jacket_img"]/@src')
        pinFen = selector.xpath(r'//*[@id="video_review"]/table/tbody/tr/td[2]/span[2]')
        riQi = selector.xpath(r'//*[@id="video_date"]/table/tbody/tr/td[2]')
        shiChang = 

#番号 ABP-525
#//*[@id="video_id"]/table/tbody/tr/td[2]
# 海报图片地址
#//*[@id="video_jacket_img"]/@src
#评分 (9.4)
#//*[@id="video_review"]/table/tbody/tr/td[2]/span[2]
#日期 2016-10-11
#//*[@id="video_date"]/table/tbody/tr/td[2]
#影片时长
#//*[@id="video_length"]/table/tbody/tr/td[2]
#演员
#//span/span[1]/a
#影片类型
#//*[@id="video_genres"]/table/tbody/tr/td[2]
#想要这个影片
#//*[@id="subscribed"]/a
#看过这个影片
#//*[@id="watched"]/a
#拥有这个影片
#//*[@id="owned"]/a