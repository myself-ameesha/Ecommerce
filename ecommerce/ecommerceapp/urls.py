from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productdetails', views.productdetails, name='productdetails'),
    path('contact', views.contact, name='contact'),
    path('shopcart', views.shopcart, name='shopcart'),
    path('checkout', views.checkout, name='checkout'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('shop', views.shop, name='shop'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),

    
]