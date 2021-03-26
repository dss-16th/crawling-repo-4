import scrapy,re
from scrapy.crawler import CrawlerProcess
from covid_19_total_backup.items import Covid19TotalBackupItem

class Spider(scrapy.Spider):
    name = "covid_19_total_backup"
    start_urls =  ["http://ncov.mohw.go.kr/",
                   'http://ncv.kdca.go.kr/']
    
    def start_requests(self):  
        # link = response.xpath('/html/body/div/div[2]/div/div[2]/ul[1]/li[1]/a/@href').extract()
        yield scrapy.Request("http://ncov.mohw.go.kr/", callback=self.parse_content)
        
    def parse_content(self,response):
        item = Covid19TotalBackupItem()
        date = response.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div[1]/h2/a/span[1]/text()').extract()
        date = list(date)[0].split(" ") 
        date = date[0:3]
        date = " ".join(date)
        item['date'] = date.replace("(","21.").replace(",","")
        item['country_in'] =list(map(int, response.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[1]/span[2]/text()').extract()))
        item['country_out'] =list(map(int, response.xpath('/html/body/div/div[5]/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[2]/span[2]/text()').extract()))
        item['total_country'] = [item['country_in']+item['country_out'] for item['country_in'],item['country_out'] in zip(item['country_in'],item['country_out'])][0]
        item['capital_distance'] = response.xpath('//*[@id="main_maplayout"]/button[9]/span[2]/text()').extract()[0]
        item['noncapital_distance'] = response.xpath('//*[@id="main_maplayout"]/button[17]/span[2]/text()').extract()[0]
        meta = {'item':item}
        yield scrapy.Request('http://ncv.kdca.go.kr/',meta=meta, callback=self.parse)
    
    def parse(self, response):
        item = Covid19TotalBackupItem(response.meta['item'])
        take_yesterday_1 = response.xpath('//*[@id="content"]/div[2]/div/div/div[1]/div[1]/ul/li[2]/div/p/span/text()').extract()
        item['take_yesterday_1'] = list(take_yesterday_1)[0]
        take_yesterday_2 = response.xpath('//*[@id="content"]/div[2]/div/div/div[1]/div[2]/ul/li[2]/div/p/span/text()').extract()
        item['take_yesterday_2'] = list(take_yesterday_2)[0]
        
        
        total_1 = response.xpath('//*[@id="content"]/div[2]/div/div/div[1]/div[1]/ul/li[1]/div/p/span[1]/text()').extract()
        item['total_1'] = list(total_1)[0]
        total_2 = response.xpath('//*[@id="content"]/div[2]/div/div/div[1]/div[2]/ul/li[1]/div/p/span[1]/text()').extract()
        item['total_2'] = list(total_2)[0]
        
        seoul_vaccine = response.xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/p[1]/span[2]/text()').extract()
        item['seoul_vaccine'] = list(seoul_vaccine)[0]
        gyeonggi_vaccine = response.xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/p[9]/span[2]/text()').extract()
        item['gyeonggi_vaccine'] = list(gyeonggi_vaccine)[0]
        incheon_vaccine = response.xpath('//*[@id="content"]/div[2]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/p[4]/span[2]/text()').extract()
        item['incheon_vaccine'] = list(incheon_vaccine)[0]
        yield item
