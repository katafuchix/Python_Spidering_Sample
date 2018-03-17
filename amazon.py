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

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'}
hdr = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.amazon.co.jp/gp/product/B00VWJYJPK/"
req = urllib.request.Request(url, headers=hdr)
#リクエストを発行し、HTMLデータを受け取る
html = urllib.request.urlopen(req)
#HTMLデータをBeautifulSoupに解釈される
bs = BeautifulSoup(html, "html.parser")
title = bs.find('h1').getText()

print(title)

print( bs.find('#priceblock_ourprice') )

#priceDisp = bs.find('b',{'class':'priceLarge'})
priceDisp = bs.find('span',{'class':'a-size-medium a-color-price'})
print(priceDisp)

priceDisp = bs.find('span',{'class':'a-size-medium a-color-price'}).getText()
print(priceDisp)
