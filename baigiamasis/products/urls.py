from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_products, name='scrape_products'),
    path('scrape/recipes/?P<str:product_name>/', views.scrape_recipes, name='scrape_recipes'),
]
