import scrapy
from scrapy.loader import ItemLoader
from GB_scraper.items import Part


class GBSpider(scrapy.Spider):
    name = 'GB'
    start_urls = [
		'https://www.gobilda.com/motion',
		'https://www.gobilda.com/structure/',
		'https://www.gobilda.com/electronics/',
		'https://www.gobilda.com/hardware/',
	]

    def parse(self, response):
        # Get the product box
        parts = response.css('li.product')
        # links = products.css('a').attrib['href']
        if parts: # exists
            # Sometimes, catalog pages are within others, so we have to recursively
			# go through each page to get to actual parts
            yield from response.follow_all(parts, self.parse)
        else:
            yield self,parse_part_page(response)

    
    def parse_part_page(self, response):
        name = response.css( 'h1.productView-title').get()
        print(name)
		# if step_file and 'Bundle' not in name: # bundles will contain repeats, we don't want that
		# 	loader = ItemLoader(Product(), response=response)
		# 	loader.add_css('sku', 'span.productView-sku-input::text')
		# 	loader.add_value('file_urls', [f'https://www.gobilda.com{step_file}'])
		# 	loader.add_value('name', name)
		# 	return loader.load_item()
