
import scrapy
from datetime import datetime
from covid_support.items import CovidSupportItem

class CovidSpider(scrapy.Spider):
    name = 'CovidSupport'
    allow_domain = ['https://www.naver.com/']
    
    def start_requests(self):
        yield scrapy.Request("https://search.naver.com/search.naver?where=news&query=코로나%20서울%20경기%20재난지원금&pd=4", callback=self.parse_kword)
        
    def parse_kword(self, response):
        item = CovidSupportItem()
        now = datetime.now()
        #item['date'] = "%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute)
        item['date'] = "%s.%s.%s %s:%s" %(now.year, now.month, now.day, now.hour, now.minute)
        support_title = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@title').extract()
        support_link = response.xpath('//*[@id="main_pack"]/section/div/div[3]/ul/li/div[1]/div/a/@href').extract()
        for i in range(len(support_title)):
            item['title']= support_title[i]
            item['link'] = support_link[i]
            yield item
