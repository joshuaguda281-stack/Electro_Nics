from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('single/', views.single, name='single'),
    path('bestseller/', views.bestseller, name='bestseller'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('404/', views.page_not_found, name='error404'),
    path('contact/', views.contact, name='contact'),
]


