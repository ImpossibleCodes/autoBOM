# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Part Info object that yield all the neccesary info related to that part
class Part(scrapy.Item):
    name = scrapy.Field() # formal part Name 
    sku = scrapy.Field() # stock keeping unit number
    price = scrapy.Field() # price of the product before tax and discounts
    url = scrapy.Field() # uniform resource locator aka link to reach the product page
    status = scrapy.Field() # status of the part (whether the parts is In Stock or not)
