
import scrapy
from datetime import datetime
from covid_soc_distance.items import CovidSocDistanceItem

class CovidSpider(scrapy.Spider):
    name = 'CovidSocDistance'
    allow_domain = ['https://www.naver.com/']
    
    def start_requests(self):
        yield scrapy.Request("https://search.naver.com/search.naver?where=news&query=코로나%20사회적거리두기&pd=4", callback=self.parse_kword)
        
    def parse_kword(self, response):
        item = CovidSocDistanceItem()
        now = datetime.now()
        #item['date'] = "%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute)
        item['date'] = "%s.%s.%s %s:%s" %(now.year, now.month, now.day, now.hour, now.minute)
        soc_distance_title = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@title').extract()
        soc_distance_link = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@href').extract()
        for i in range(len(soc_distance_title)):
            item['title']= soc_distance_title[i]
            item['link'] = soc_distance_link[i]
            yield item
