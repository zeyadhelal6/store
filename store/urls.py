from .views import allproducts
from django.urls import path




urlpatterns = [
    path('', allproducts,  name='products')
]