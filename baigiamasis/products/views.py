from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . import models
import urllib.parse
from django.shortcuts import render

def scrape_products(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.find_all('div', class_='js-product-container card -horizontal-for-mobile')

    products = []

    for product_element in product_elements:
        product_name = product_element.find('p', class_='card__name').text
        product_price = product_element.find('div', class_='price-tag card__price').text
        product_image = product_element.find('img')['src']


        products.append(models.ScrapedProduct(product_name, product_price, product_image))

    return products


def scrape_recipes(product_name):
    url = 'https://www.receptai.lt/paieska?'
    params = {'q': product_name}


    response = requests.get(url + urllib.parse.urlencode(params))
    soup = BeautifulSoup(response.content, 'html.parser')

    recipes_elements = soup.find_all('div', class_='item')

    recipes = []

    for recipes_element in recipes_elements:
        recipes_title = recipes_element.find('img')['alt']
        recipes_image = recipes_element.find('img')['src']
        recipes_link = recipes_element.find('a')['href']



        recipes.append(models.ScrapedRecipes(recipes_title, recipes_image, recipes_link))

    return recipes


def index(request):
    chicken_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3Acategory%3A%25C5%25A0vie%25C5%25BEia%2Bpauk%25C5%25A1tiena"
    fish_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3Acategory%3A%25C5%25A0vie%25C5%25BEios%2B%25C5%25BEuvys%2Bir%2Bj%25C5%25ABr%25C5%25B3%2Bg%25C4%2597ryb%25C4%2597s"
    pork_and_beef_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3Acategory%3A%25C5%25A0vie%25C5%25BEia%2Bm%25C4%2597sa"
    processed_meat_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3Acategory%3AApdorotos%2Bm%25C4%2597sos%2Bir%2Bpauk%25C5%25A1tienos%2Bgaminiai%2B"
    processed_fish_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3AfixedPrice%3Afalse%3Acategory%3AApdorotos%2B%25C5%25BEuvies%2Bgaminiai"
    products = []
    recipes = []

    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'chicken':
        products = scrape_products(chicken_url)
    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'fish':
        products = scrape_products(fish_url)
    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'pork_and_beef':
        products = scrape_products(pork_and_beef_url)
    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'processed_meat':
        products = scrape_products(processed_meat_url)
    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'processed_fish':
        products = scrape_products(processed_fish_url)


    if request.method == 'GET' and 'product_name' in request.GET:
        recipes = scrape_recipes(request.GET.get('product_name'))



    return render(request, 'products/scraper.html', {'products': products, 'recipes': recipes})

def contact(request):
    return render(request, 'products/contacts.html')