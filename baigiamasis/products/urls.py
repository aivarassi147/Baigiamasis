from django.urls import path
from . import views

urlpatterns = [
    path('scrape', views.index, name='scrape_products'),
    path('contact/', views.contact, name='contact'),
]
