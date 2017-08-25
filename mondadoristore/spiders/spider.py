
import scrapy
from mondadoristore.items import MondadoristoreItem
import os,openpyxl
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MySpider(scrapy.Spider):
    name = 'mondadoristore'
    allowed_domains = ['mondadoristore.com']
    start_urls = []
    os.chdir(os.getcwd())
    # with open('Input.txt' , 'rb') as file:
    #     lines = file.readlines()
    # new_lines = [line.strip()[:-1] for line in lines]

    base_URL = 'http://www.mondadoristore.it/pd/eai'


    lines = []
    wb = openpyxl.load_workbook("Input.xlsx")
    ws = wb['All_Scrapping']
    for line in ws['A']:
        lines.append(str(line.value).strip())
    new_lines = [line.strip()[:-1] for line in lines]

    for line in new_lines:
        start_urls.append(base_URL+line)

    def parse(self, response):        
        item = MondadoristoreItem()        
        item['url'] = response.url
        item['isbn'] = self.lines[self.new_lines.index(response.url.split('/eai')[-1][:-1])]   

        price1 = response.xpath('//span[@class="new-price new-detail-price"]/strong/text()').extract_first().replace(',','.')
        price2 = response.xpath('//span[@class="new-price new-detail-price"]/strong/span[@class="decimals"]/text()').extract_first()

        item['price'] = price1 + price2
        yield item