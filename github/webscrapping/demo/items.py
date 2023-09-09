# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DemoItem(scrapy.Item):
    #product related items, such as id,name,price
    #productId=Field()
    productName=Field()
    price=Field()
    
    #items to store links
    productLink=Field()
    
    #item for company name
    #website = Field()
    pass

