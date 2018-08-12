import scrapy
from elasticsearch import Elasticsearch
import requests
import json

class PriceSpider(scrapy.Spider):
    name = "prices"
    elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    elasticServer = 'http://localhost:9200'
    peopleApi = 'http://swapi.co/api/people/'

    def start_requests(self):
        request = requests.get(self.elasticServer)
        index = 1
        while request.status_code == 200:
            request = requests.get(self.peopleApi + str(index))
            self.elastic.index(index='starwars', doc_type='people', id=index, body=json.loads(request.content))
            index = index + 1
            print('========================================>>' + str(index))

