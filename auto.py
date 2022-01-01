import scraping
import config

class Auto:
    def scraping(self):
        data = config.Config()
        data = data.getData()
        thread = []
        for i in range(len(data[0])):
            scr = scraping.Scraping()
            thread += scr.getThread(data[0][i],data[1][i])
        thread.sort()

        return thread