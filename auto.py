import scraping
import config

class Auto:
    def scraping(self):
        contents = []
        for i in range(100):
            scr = scraping.Scraping()
            print(i+1,'番目　hawk:0 その他:1 終わり:9')
            pattern = config.htmlPattern()
            if(pattern == 9):
                break
            contents += scr.getThread(pattern,config.urls(),config.startTime())
        thread = []
        thread = sorted(contents)
        print(thread)
        return thread

    # def scraping():
    #     urls= config.urls

    #     for url in urls:
    #         scr = Scraping(url,今か昔,開始時間)
    #         contents[]
    #         contents.append(scr)
        
    #     thread = contents.sort()

    #     return thread