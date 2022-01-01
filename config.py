class Config:
    def getData(self):
        urls = []
        startTimes = []
        print('スタート時間(8時30分→0830)')
        startTime = input()
        i = 1
        while True:
            print(i, '番目：URL?')
            url = input()
            if(url == '9'):
                return [urls,startTimes]
            elif(url[0] == 'h'):
                urls.append(url)
                startTimes.append(startTime)
                i += 1
            else:
                startTime = url
                print('開始時間を', startTime, 'に変更しました')