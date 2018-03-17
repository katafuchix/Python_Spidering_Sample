# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import time
import sys
import re
#from sqlalchemy.orm import joinedload
#from db import db_session, init_db
#from models import ItemsDigitalVideoa
from datetime import datetime
from time import sleep
import random


def getReleaseDate(str):
    date_pattern = re.compile('(\d{4})/(\d{1,2})/(\d{1,2})')
    result = date_pattern.search(str)
    #print(result.group())
    if result:
        return result.group()
    else:
        return ""

def getInfo(url):
    req = urllib.request.Request(url)
    #リクエストを発行し、HTMLデータを受け取る
    html = urllib.request.urlopen(req)
    #HTMLデータをBeautifulSoupに解釈される
    bs = BeautifulSoup(html, "html.parser")
    title = bs.find('h1').getText()
    img = ''
    image = bs.select('#sample-video')[0].find('a')
    #print(image)
    if image != None:
        img = image.get("href")

    #desc = bs.find('div', class_='lh4').find('p', class_='mg-b20').getText()
    #desc = bs.find('p', class_='mg-b20').getText()
    desc = bs.find('div', class_='lh4').getText()
    if desc != '':
        desc = desc.strip().replace('\n','').replace('\r','')
        print(desc)

    table = bs.find('table', class_='mg-b12').find('table', class_='mg-b20')
    idol = ''
    releaseDate = ''
    genre = ''
    maker = ''
    label = ''
    itemNo = ''
    videoTime = ''
    series = ''
    try:
        for tr in table.find_all('tr'):
            date = getReleaseDate(tr.getText().strip().replace('\n','').replace('\r',''))
            if date != "":
                releaseDate = date
            td = tr.find_all('td')
            #print(td)
            #print(len(td))
            if len(td) == 2 :
                #print('------')
                td0 = td[0].getText()
                td1 = td[1].getText()
                    #print(td0)
                    #print(td1)
                if td0.find('出演者') > -1:
                    idol = td1.strip().replace('\n','').replace('\r','')
                    #if td0.find('配信開始日') > -1:
                    #    releaseDate = td1.strip().replace('\n','').replace('\r','')
                if td0.find('ジャンル') > -1:
                    genre = td1.strip().replace('\n','').replace('\r','')
                if td0.find('メーカー') > -1:
                    maker = td1.strip().replace('\n','').replace('\r','')
                if td0.find('品番') > -1:
                    itemNO = td1.strip().replace('\n','').replace('\r','')
                if td0.find('収録時間') > -1:
                    videoTime = td1.strip().replace('\n','').replace('\r','')
                if td0.find('シリーズ：') > -1:
                    series = td1.strip().replace('\n','').replace('\r','')
                if td0.find('レーベル：') > -1:
                    label = td1.strip().replace('\n','').replace('\r','')
    except:
        print('エラー発生')
    return (title, desc, img, idol, genre, series, releaseDate, maker, label, itemNo, videoTime)


def getPage(url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=hdr)
    #リクエストを発行し、HTMLデータを受け取る
    html = urllib.request.urlopen(req)
    #HTMLデータをBeautifulSoupに解釈される
    bs = BeautifulSoup(html, "html.parser")

    #for a in bs.find_all(class_="tmb"):
    for li in bs.find_all('li'):
        #print( isinstance(a,type(None)))
        a = li.find(class_="tmb")
        if a == None:
            continue
        #print(a)
        prices = li.find_all('p', class_="price")
        #tmp = price.split('～')
        #if len(tmp)>1:
        #    price = tmp[0]+"～"
        #print(prices[0])
        #print(prices[1])
        price = prices[0].getText().strip().replace('\n','').replace('\r','')
        used_price = ""
        try:
            used_price = prices[1].getText().strip().replace('\n','').replace('\r','')
        except:
            print("used_price err")
        print(price)
        print(used_price)

        off = prices = li.find('p', class_="price").find('span').getText().strip().replace('\n','').replace('\r','')
        print(off)
        #continue

        rate = li.find(class_="rate").getText()
        print(rate)
        iurl = a.find('a').get("href").rstrip()
        iurls = iurl.split('?')
        iurl = iurls[0]
        print(iurl)
        #continue

        #r = ItemsDigitalVideoa.query.filter(ItemsDigitalVideoa.link.contains(iurl)).all()
        #if len(r)>0:
        #    continue

        title, desc, img, idol, genre, series, releaseDate, maker, label, itemNo, videoTime = getInfo(iurl)
        if img == "":
            continue
        print(title)
        print(img)
        print(idol)
        print(genre)
        print(releaseDate)
        print(a.find('a').get("href").rstrip())
        print(a.select(".txt")[0].getText())
        #continue

url = "http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=13gvg00358/"

title, desc, img, idol, genre, series, releaseDate, maker, label, itemNo, videoTime = getInfo(url)
print(title)
print(img)
print(idol)
print(genre)
print(releaseDate)
