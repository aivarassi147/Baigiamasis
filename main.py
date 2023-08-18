from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import time
from . import models
import urllib.parse

def scrape_products(request):
    url = 'https://www.rimi.lt/e-parduotuve/lt/akcijos?page=1&pageSize=100&query=%3Arelevance%3AassortmentStatus%3AinAssortment%3AinStockFlag%3Atrue%3AfixedPrice%3Afalse%3AfirstLevelCategory%3AM%25C4%2597sa%252C%2B%25C5%25BEuvys%2Bir%2Bkulinarija'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_elements = soup.find_all('div', class_='js-product-container card -horizontal-for-mobile')

        products = []

        for product_element in product_elements:
            product_name = product_element.find('p', class_='card__name').text
            product_price = product_element.find('div', class_='price-tag card__price').text
            product_image = product_element.find('img')['src']


            products.append(models.ScrapedProduct(product_name, product_price, product_image))

        return render(request, 'products/scraper.html', {'products': products})


def scrape_recipes(request, product_title):
    url = 'https://www.receptai.lt/paieska?'
    params = {'q': 'product_name'}


    response = requests.get(url + urllib.parse.urlencode(params))
    soup = BeautifulSoup(response.content, 'html.parser')

    product_elements = soup.find_all('div', class_='list')

    recipes = []

    for product_element in product_elements:
        product_title = product_element.find('div', class_='a').text


        recipes.append(models.ScrapedRecipes(product_title))

    return render(request, 'recipes/scraper.html', {'recipes': recipes})
