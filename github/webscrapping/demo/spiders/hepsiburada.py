import scrapy
from demo.items import DemoItem
from scrapy.http import Request
import csv

class HepsiburadaSpider(scrapy.Spider):
    name = 'hepsiburada'
    allowed_domains = ['hepsiburada.com']
    start_urls = ['http://hepsiburada.com/']
    def start_requests(self):	
        with open("/Users/tunab/Downloads/Newfolder/demo/csv/hepsiburada.csv", "rU") as f:
            reader=csv.DictReader(f)
            for row in reader:
                url=row['url']
                i=1
                page=i
                link_urls = [url.format(i) for i in range(i,50)]	
                for link_url in link_urls:
                    request=Request(link_url, callback=self.parse_product_pages, meta={'page': page})
                    page+=1
                    yield request

    def parse_product_pages(self,response):
        item=DemoItem()
        content=response.xpath('//*[@id="'+str(response.meta['page'])+'"]')
        #f = open("demofile2.txt", "a")
        #f.write(str(content.getall()))
        #f.close()
        for product_content in content.xpath('./li[@class="productListContent-item"]'):
            #item['productId']=product_content.xpath('.//@id').get()+'_'+str(response.meta['category'])+'_hepsiburada'
            item['productName']=product_content.xpath('.//*[@data-test-id="product-card-name"]/text()').get()		
            item['price']=product_content.xpath('.//*[@data-test-id="price-current-price"]/text()').get()
            item['productLink']=product_content.xpath('.//a/@href').get()	
            #item['website']="Hepsiburada"	
            if item['productName']==None:
                    break
            yield (item)
            
    def parse(self, response):
        pass
