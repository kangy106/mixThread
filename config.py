class Config:
    def getData(self):
        patterns = []
        urls = []
        startTimes = []
        for i in range(100):
            print(i+1,'番目　hawk:0 その他:1 終わり:9')
            pattern = int(input())
            if(pattern == 9):
                return [patterns,urls,startTimes]
            patterns.append(pattern)

            print('URL?')
            urls.append(input())

            print('スタート時間(8時30分→0830)')
            startTimes.append(input())    