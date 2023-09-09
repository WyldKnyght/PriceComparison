import scrapy
from demo.items import DemoItem
from scrapy.http import Request
import csv


class GittigidiyorSpider(scrapy.Spider):
    name = 'gittigidiyor'
    allowed_domains = ['gittigidiyor.com']
    start_urls = ['http://gittigidiyor.com/']
    def start_requests(self):	
        with open("/Users/tunab/Downloads/Newfolder/demo/csv/gittigidiyor.csv", "rU") as f:
            reader=csv.DictReader(f)
            i=1
            for row in reader:
                url=row['url']
                #max_page=int(row['page'])
                link_urls = [url.format(i) for i in range(i,99)]
                for link_url in link_urls:

                    yield Request(link_url, callback=self.parse_product_pages)
    def parse_product_pages(self,response):

        item=DemoItem()

        content=response.xpath('//*[@data-testid="content"]')
        #content2=response.xpath('/body')
        #f = open("demofile2.txt", "a", encoding="utf-8")
        #f.write(str(content.getall()))
        #f.close()

        for product_content in content.xpath('.//ul/li'):
        #for product_content in content.xpath('//*[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]'):
            #print("----------------------------------")

            item['productName']=product_content.xpath('.//h3/text()').get()
            item['price']=str(product_content.xpath('.//*[@class="buy-price"]/text()').get()).replace(u'\n', u'').replace(' ', '').replace('\t', '').replace('TL', '')
            item['productLink']=product_content.xpath('.//a/@href').get()
            #print(product_content.xpath('.//h2/text()').getall())
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
