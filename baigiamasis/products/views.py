from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from . import models
import urllib.parse

def scrape_products(url):
    # url = 'https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija'

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
    url = 'https://www.receptai.lt/paieska?file'
    params = {'q': product_name}


    response = requests.get(url + urllib.parse.urlencode(params))
    soup = BeautifulSoup(response.content, 'html.parser')

    recipes_elements = soup.find_all('div', class_='item')

    recipes = []

    for recipes_element in recipes_elements:
        print(recipes_element.find('img'))
        recipes_title = recipes_element.find('img')['alt']



        recipes.append(models.ScrapedRecipes(recipes_title))

    return recipes


def index(request):
    mesos_url = "https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=20&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija"
    products = []
    recipes = []

    if request.method == 'GET' and 'product_type' in request.GET and request.GET.get('product_type') == 'mesa':
        products = scrape_products(mesos_url)



    if request.method == 'GET' and 'product_name' in request.GET:
        recipes = scrape_recipes(request.GET.get('product_name'))



    return render(request, 'products/scraper.html', {'products': products, 'recipes': recipes})

def contact(request):
    return render(request, 'products/contacts.html')