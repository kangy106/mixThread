import requests
import time
from bs4 import BeautifulSoup
import re
import datetime

class Scraping:
    def getThread(self,pattern,url,start):
        res=requests.get(url)
        thread = []
        if pattern == 0:
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, 'lxml')

            threadRes=soup.find_all('dd')
            threadTime=soup.find_all('dt')

            for i in range(len(threadTime)):
                num = int(re.sub('ID:[\w/+]+|\D|<[^<>]*>',"",str(threadTime[i])))%10000000000000000
                if num < 1000000000000000:
                    continue
                d = int(num%10000000000/100000000)
                h = int(num%100000000/1000000)
                m = int(num%1000000/10000)
                s = int(num%10000/100)
                ms = int(num%100)
                try:
                    time_ = datetime.datetime(2000,1,d,h,m,s,ms*10000)
                except ValueError:
                    continue
                s = datetime.timedelta(days= d - 1,minutes = int(start)%100,hours = int(int(start)/100))

                tuple = (time_-s,re.sub('<[^<>]*>|\n|&gt;&gt;[0-9]+',"",str(threadRes[i])))
                thread.append(tuple)
        elif int(pattern) == 1:
            res.encoding = res.apparent_encoding
            soup = BeautifulSoup(res.text, 'html.parser')
            threadRes = soup.select('span.escaped')
            threadTime = soup.select('span.date')
            for i in range(len(threadTime)):
                num = int(re.sub(r'\D',"",threadTime[i].contents[0]))
                if num < 1000000000000000:
                    continue
                d = int(num%10000000000/100000000)
                h = int(num%100000000/1000000)
                m = int(num%1000000/10000)
                s = int(num%10000/100)
                ms = int(num%100)
                try:
                    time_ = datetime.datetime(2000,1,d,h,m,s,ms*10000)
                except ValueError:
                    continue
                s = datetime.timedelta(days= d - 1,minutes = int(start)%100,hours = int(int(start)/100))
                tuple = (time_-s,threadRes[i].get_text())
                thread.append(tuple)
        return thread

