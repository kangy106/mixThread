import datetime
import msvcrt
import time

class Display:
    def execution(self,thread):
        stime = time.time()
        times = datetime.datetime(2000,1,1,0,0,0,0)
        i = 0
        while True:
            if(thread[i][0] < times):
                try:
                    print(i,':',thread[i][0],':','\n',thread[i][1], '\n','\n',sep='')
                except UnicodeEncodeError:
                    print('\n','\n')
                i += 1
            else:
                break

        sleepTime = 0.08
        while True:
            time.sleep(sleepTime)
            mtime = time.time()
            if(thread[i][0]<=times + datetime.timedelta(seconds=mtime-stime)):
                try:
                    print(i,':',thread[i][0],':','\n',thread[i][1], '\n','\n',sep='')
                except UnicodeEncodeError:
                    print('\n','\n')
                i += 1
            if msvcrt.kbhit(): # キーが押されているか
                kb = msvcrt.getch() # 押されていれば、キーを取得する
                if str(kb) == 'b\' \'': # str必要
                    stopStart = time.time()
                    while True:
                        if msvcrt.kbhit(): # キーが押されているか
                            kb = msvcrt.getch() # 押されていれば、キーを取得する
                            if str(kb) == 'b\' \'': # str必要
                                stopEnd = time.time()
                                print(stopEnd-stopStart)
                                times -= datetime.timedelta(seconds=stopEnd-stopStart)
                                break

                elif str(kb) == 'b\'j\'':
                    times -= datetime.timedelta(seconds=5)
                elif str(kb) == 'b\'l\'':
                    times += datetime.timedelta(seconds=5)
                elif str(kb) == 'b\'s\'':
                    sleepTime += 0.01
                    print(sleepTime)
                elif str(kb) == 'b\'q\'':
                    sleepTime -= 0.01
                    print(sleepTime)
