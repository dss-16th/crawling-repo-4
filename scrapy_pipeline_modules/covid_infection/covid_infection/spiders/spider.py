
import scrapy
from datetime import datetime
from covid_infection.items import CovidInfectionItem

class CovidSpider(scrapy.Spider):
    name = 'CovidInfection'
    allow_domain = ['https://www.naver.com/']
    
    def start_requests(self):
        yield scrapy.Request("https://search.naver.com/search.naver?where=news&query=코로나%20수도권%20확진&pd=4", callback=self.parse_kword)
        
    def parse_kword(self, response):
        item = CovidInfectionItem()
        now = datetime.now()
        #item['date'] = "%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute)
        item['date'] = "%s.%s.%s %s:%s" %(now.year, now.month, now.day, now.hour, now.minute)
        infection_title = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@title').extract()
        infection_link = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@href').extract()
        for i in range(len(infection_title)):
            item['title']= infection_title[i]
            item['link'] = infection_link[i]
            yield item
