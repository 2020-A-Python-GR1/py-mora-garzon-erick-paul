import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product.pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()

        print(titulos)
# scrapy scrawl nombre_arania



def guardar_archivo(titulo, precio, links):
    import csv
    with open('libros.csv','a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulo, precio, links))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)

def escribir_archivo(ruta_archivo, lineas_a_escribir):
    try:
        archivo_escritura = open(ruta_archivo, mode="a")
        archivo_escritura.writelines(lineas_a_escribir)
        archivo_escritura.close()
    except Exception as error:
        print('Error archivo', error)

def guardar_txt(titulos, precios, links_imagenes):
    path_archivo = "./books.txt"
    books = []
    for x in range(0, len(titulos)):
        book = "\nTitulo: " + titulos[x] + "\n" + "Precio: " + precios[x] + "\n" + "URL imagen: " + links_imagenes[x] + "\n"
        books.append(book)
    escribir_archivo(path_archivo, books)

def priceToFloat(price):
    return float(price[1:])

def transformImageToLink(image_link):
    image_link = image_link[12:]
    return image_link

    def parse_categories_links(self, response):
        books_urls = response.css("div.side_categories > ul > li > ul > li > a::attr(href)").extract()
        def transformBooksToLink(book_link):
            if(book_link != 'index.html'):
                book_link = book_link[3:]
            return self.url_base + book_link

        books_full_url = list(map(transformBooksToLink, books_urls))
        for url in books_full_url:
            yield scrapy.Request(url=url, callback=self.parse_books)

    def parse_books(self, response):
        
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css("h3 > a::text").extract()
        precios = etiqueta_contenedora.css("div.product_price > p.price_color::text").extract()
        imagenes = etiqueta_contenedora.css("div.image_container > a > img::attr(src)").extract()

        precios_float = list(map(priceToFloat, precios))
        links_imagenes = list(map(transformImageToLink, imagenes))

        guardar_archivo(titulos, precios, links_imagenes)
        guardar_txt(titulos, precios, links_imagenes)
