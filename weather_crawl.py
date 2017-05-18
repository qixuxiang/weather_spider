# -*- coding:utf-8 -*-
import io
import sys
import re
import codecs
import csv
import codecs
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit


Year = '2015'
strFile = 'yangzhou' + Year + '.csv'


f = codecs.open(strFile, 'w',encoding='utf-8')

f.write('strDate' +',' + 'lowWeather' +',' + 'highWeather' +','+'weather'+','+'wind_direction'+','+'wind_force' + '\n')
for month in range(1, 13):
    if(month < 10):
        strMonth = '0' + str(month)
    else:
        strMonth = str(month)
    YearMonth = Year + strMonth
    print("\nGetting data for month" + YearMonth + "...", end='')

    url  = "http://lishi.tianqi.com/yangzhou/"+YearMonth+".html"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)
    weatherSet = soup.find(attrs={"class":"tqtongji2"})
    if(weatherSet == None):
        print("fail to get the page", end='')
        continue

    for line in weatherSet.contents:
        if(line.__class__.__name__ == 'NavigableString'): continue
        if(len(line.attrs) > 0): continue
        lis = line.findAll('li')
        strDate = lis[0].text
        highWeather = lis[1].text
        lowWeather  = lis[2].text
        weather = lis[3].text
        wind_direction = lis[4].text
        wind_force = lis[5].text
        print(type(wind_force))
        print(wind_force)

        f.write(strDate +',' + lowWeather +',' + highWeather + ','+weather +','+wind_direction +','+ wind_force +'\n')
    print("done", end='')

f.close()
