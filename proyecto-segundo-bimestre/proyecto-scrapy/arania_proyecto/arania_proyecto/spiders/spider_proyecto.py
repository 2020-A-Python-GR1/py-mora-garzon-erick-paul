  
import scrapy 

def archivo(titulos,genero1,genero2,genero3,year,votos,rating,director1,director2):
    import csv
    with open('videojuegos.csv','a', newline='', encoding="utf-8") as csvfile:
        #csvfile.write('titulos,genero1,genero2,genero3,year,votos,rating,director1,director2\n')
        spamwriter = csv.writer(csvfile, delimiter=',')

        data = list(zip(titulos,genero1,genero2,genero3,year,votos,rating,director1,director2))
        for row in data:
            row = list(row)
            spamwriter.writerow(row)

class IntroSpider(scrapy.Spider):
    name = 'videojuegos_spider' 
    urls = [
        'https://www.imdb.com/search/title/?title_type=video_game&user_rating=7.0,10.0&num_votes=1000,1000000&sort=user_rating,desc&count=250',
        'https://www.imdb.com/search/title/?title_type=video_game&user_rating=7.0,10.0&num_votes=1000,1000000&sort=user_rating,desc&count=250&start=251&ref_=adv_nxt'
    ]

    

    def start_requests (self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    
    def parse(self, response):


        etiqueta_contenedora = response.css('div.lister-item')

        titulos = etiqueta_contenedora.css('h3.lister-item-header>a::text').extract() 
        print(titulos)

        genero = etiqueta_contenedora.css('p.text-muted > span.genre::text').extract()
        print(genero)

        year = etiqueta_contenedora.css('span.lister-item-year.text-muted.unbold::text').extract()
        print(year)

        votos = etiqueta_contenedora.css('p.sort-num_votes-visible > span::attr(data-value)').extract()  
        print(votos)

        rating = etiqueta_contenedora.css('div.ratings-bar > div.inline-block::attr(data-value)').extract()
        print(rating)

        director1 = etiqueta_contenedora.css('p > a:first-child::text').extract()
        print(director1)

        director2 = etiqueta_contenedora.css('p > a:nth-child(2)::text').extract()
        print(director2)
        
        year = [int(i.replace(' Video Game)', '').replace('(', '').replace('I)', '')) for i in year]
        print(year)

        votos = [int(i) for i in votos]
        print(votos)

        rating = [float(i) for i in rating]
        print(type(rating[0]))

        genero = [i.replace('\n', '').replace(' ', '') for i in genero]
        #print(genero)

        genero1 = [i.split(',')[0] for i in genero]
        #print(genero1)

        genero_aux = [i.split(',') for i in genero]
        #print(genero_aux)

        genero2 = [i[1:2] for i in genero_aux]
        #print(genero2)

        genero2 = [str(i).replace('[', '').replace(']', '').replace("'", '') for i in genero2]
        #print(genero2)

        genero3 = [i[2:3] for i in genero_aux]
        #print(genero3)

        genero3 = [str(i).replace('[', '').replace(']', '').replace("'", '') for i in genero3]
        #print(genero3)
   
           

       
        archivo(titulos,genero1,genero2,genero3,year,votos,rating,director1,director2)