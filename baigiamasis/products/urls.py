from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrape_products, name='scrape_products'),
    path('scrape/recipes/', views.scrape_recipes, name='scrape_recipes'),
]
