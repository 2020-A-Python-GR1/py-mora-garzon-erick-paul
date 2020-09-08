import scrapy
from arania_fybeca.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaFybeca(scrapy.Spider):
    name = "fybeca"
    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url)

    def parse(self, response):
        productos = response.css('div.product-tile-inner')
        for producto in productos:
            detalles = producto.css('div.detail')
            tiene_detalle = len(detalles) > 0
            if(tiene_detalle):
                producto_loader = ItemLoader(
                item = ProductoFybeca(),
                selector = producto
                )
                # producto_loader.default_output_processor=TakeFirst()
                
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )

                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )
                yield producto_loader.load_item() 