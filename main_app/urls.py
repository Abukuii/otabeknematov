from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Login
    path('login', login_page, name='login'),

    # Home
    path('', main_page, name='home'),

    # Sale
    path('sale_page', sale_page, name='sale_page'),

    # Products
    path('products_page', products_page, name='products_page'),

    # Debtors
    path('debtors_page', debtors_page, name='debtors_page'),

    # Reduced Products
    path('reduced_products_page', reduced_products_page, name='reduced_products_page'),

    # Profile
    path('profile', profile_page, name='profile'),
]