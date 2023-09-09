import scrapy
from demo.items import DemoItem
from scrapy.http import Request
import csv

class N11Spider(scrapy.Spider):
    name = 'n11'
    allowed_domains = ['n11.com']
    start_urls = ['http://n11.com/']
    def start_requests(self):	
        with open("/Users/tunab/Downloads/Newfolder/demo/csv/n11.csv", "rU") as f:
            reader=csv.DictReader(f)
            i=1
            for row in reader:
                url=row['url']
                #max_page=int(row['page'])
                link_urls = [url.format(i) for i in range(i,50)]
                for link_url in link_urls:

                    yield Request(link_url, callback=self.parse_product_pages)
    def parse_product_pages(self,response):

        item=DemoItem()

        content=response.xpath('//*[@class="listView"]')
        #content2=response.xpath('/body')
        #f = open("demofile2.txt", "a", encoding="utf-8")
        #f.write(str(content.getall()))
        #f.close()

        for product_content in content.xpath('./ul/li'):
        #for product_content in content.xpath('//*[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]'):
            #print("----------------------------------")

            item['productName']=product_content.xpath('.//a[@class="plink"]/@title').get()
            item['price']=product_content.xpath('.//*[@class="newPrice cPoint priceEventClick"]/ins/text()').get()
            item['productLink']=product_content.xpath('.//a[@class="plink"]/@href').get()
            #print(item['productName'])
            #print(item['price'])
            #print(item['productLink'])
            #print(str(product_content.getall()))

            #f = open("demofile2.txt", "a", encoding="utf-8")
            #f.write(str(product_content.getall()))
            #f.close()
            if item['productName'] is None:
                break
            yield (item)
    def parse(self, response):
        pass
