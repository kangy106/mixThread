class mixThread:
    auto = Auto()
    thread = Thread(auto.scraping())
    display = Display()
    display.execution(thread)

    


# import 
# import time
# from bs4 import BeautifulSoup
# import re
# import datetime
# import msvcrt
# class Thread:
#     res_ = None
#     time_ = None

# th = []
# for i in range(100):
#     print(i+1,'番目　hawk:0 その他:1 終わり:9')
#     pattern = input()
#     if int(pattern) == 9:
#         break
#     print('URL?')
#     url = input()
#     print('スタート時間(8時30分→0830)')
#     start = input()
#     res=requests.get(url)
#     if int(pattern) == 0:
#         res.encoding = res.apparent_encoding
#         soup = BeautifulSoup(res.text, 'lxml')

#         thread = Thread()
#         thread.res_=soup.find_all('dd')
#         thread.time_=soup.find_all('dt')

#         for i in range(len(thread.time_)):
#             num = int(re.sub('ID:[\w/+]+|\D|<[^<>]*>',"",str(thread.time_[i])))%10000000000000000
#             if num < 1000000000000000:
#                 continue
#             d = int(num%10000000000/100000000)
#             h = int(num%100000000/1000000)
#             m = int(num%1000000/10000)
#             s = int(num%10000/100)
#             ms = int(num%100)
#             try:
#                 time_ = datetime.datetime(2000,1,d,h,m,s,ms*10000)
#             except ValueError:
#                 continue
#             s = datetime.timedelta(days= d - 1,minutes = int(start)%100,hours = int(int(start)/100))

#             tuple = (time_-s,re.sub('<[^<>]*>|\n|&gt;&gt;[0-9]+',"",str(thread.res_[i])))
#             th.append(tuple)
#     elif int(pattern) == 1:
#         res.encoding = res.apparent_encoding
#         soup = BeautifulSoup(res.text, 'html.parser')
#         thread = Thread()
#         thread.res_ = soup.select('span.escaped')
#         thread.time_ = soup.select('span.date')
#         for i in range(len(thread.time_)):
#             num = int(re.sub(r'\D',"",thread.time_[i].contents[0]))
#             if num < 1000000000000000:
#                 continue
#             d = int(num%10000000000/100000000)
#             h = int(num%100000000/1000000)
#             m = int(num%1000000/10000)
#             s = int(num%10000/100)
#             ms = int(num%100)
#             try:
#                 time_ = datetime.datetime(2000,1,d,h,m,s,ms*10000)
#             except ValueError:
#                 continue
#             s = datetime.timedelta(days= d - 1,minutes = int(start)%100,hours = int(int(start)/100))
#             tuple = (time_-s,thread.res_[i].get_text())
#             th.append(tuple)

# th2=[]
# th2=sorted(th)
# stime = time.time()
# times = datetime.datetime(2000,1,1,0,0,0,0)
# i = 0
# while True:
#     if(th2[i][0] < times):
#         try:
#             print(i,':',th2[i][0],':','\n',th2[i][1], '\n','\n',sep='')
#         except UnicodeEncodeError:
#             print('\n','\n')
#         i += 1
#     else:
#         break

# sleepTime = 0.08
# while True:
#     time.sleep(sleepTime)
#     mtime = time.time()
#     if(th2[i][0]<=times + datetime.timedelta(seconds=mtime-stime)):
#         try:
#             print(i,':',th2[i][0],':','\n',th2[i][1], '\n','\n',sep='')
#         except UnicodeEncodeError:
#             print('\n','\n')
#         i += 1
#     if msvcrt.kbhit(): # キーが押されているか
#         kb = msvcrt.getch() # 押されていれば、キーを取得する
#         if str(kb) == 'b\' \'': # str必要
#             stopStart = time.time()
#             while True:
#                 if msvcrt.kbhit(): # キーが押されているか
#                     kb = msvcrt.getch() # 押されていれば、キーを取得する
#                     if str(kb) == 'b\' \'': # str必要
#                         stopEnd = time.time()
#                         print(stopEnd-stopStart)
#                         times -= datetime.timedelta(seconds=stopEnd-stopStart)
#                         break

#         elif str(kb) == 'b\'j\'':
#             times -= datetime.timedelta(seconds=5)
#         elif str(kb) == 'b\'l\'':
#             times += datetime.timedelta(seconds=5)
#         elif str(kb) == 'b\'s\'':
#             sleepTime += 0.01
#             print(sleepTime)
#         elif str(kb) == 'b\'q\'':
#             sleepTime -= 0.01
#             print(sleepTime)
