import scrapy

class Imtec:
	def parse_urls(self):
		urls = [
			'https://imtec.ba/1273-mobiteli',
			'https://imtec.ba/1273-mobiteli?p=2'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
	
	def parse(self, response):
		filename = 'proba.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
