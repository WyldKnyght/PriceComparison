import scrapy
from demo.items import DemoItem
from scrapy.http import Request
import csv


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com.tr']
    start_urls = ['http://amazon.com.tr/']

    def start_requests(self):	
        with open("/Users/tunab/Downloads/Newfolder/demo/csv/amazon.csv", "rU") as f:
            reader=csv.DictReader(f)
            i=1
            for row in reader:
                url=row['url']
                max_page=int(row['page'])
                link_urls = [url.format(i) for i in range(i,max_page)]
                for link_url in link_urls:

                    yield Request(link_url, callback=self.parse_product_pages)
    def parse_product_pages(self,response):

        item=DemoItem()

        content=response.xpath('//*[@class="s-main-slot s-result-list s-search-results sg-row"]')
        #content2=response.xpath('/body')
        #f = open("demofile2.txt", "a", encoding="utf-8")
        #f.write(content.text)
        #f.close()

        for product_content in content.xpath('//*[@data-component-type="s-search-result"]'):
        #for product_content in content.xpath('//*[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"]'):
            #print("----------------------------------")

            item['productName']=product_content.xpath('.//*[@class="a-size-base-plus a-color-base a-text-normal"]/text()').get()
            item['price']=str(product_content.xpath('.//*[@class="a-price"]/span/text()').get()).replace(u'\xa0TL', u'')
            item['productLink']="https://www.amazon.com.tr"+str(product_content.xpath('.//a[@class="a-link-normal a-text-normal"]/@href').get()).split('/ref=')[0]
            #print(item['productName'])
            #print(item['price'])
            #print(item['productLink'])

            #f = open("demofile2.txt", "a", encoding="utf-8")
            #f.write(str(product_content.getall()))
            #f.close()
            if item['productName'] is None:
                break
            yield (item)
    def parse(self, response):
        pass
