from django.shortcuts import render, redirect
from store.models import Product


# Create your views here.
def index(request):
    products = Product.objects.all().filter(is_available=True)
    context={
        'products':products,
        }
    return render(request,'index.html',context)

def productdetails(request):
    return render(request,'productdetails.html')

def contact(request):
    return render(request,'contact.html')

def shopcart(request):
    return render(request,'shopcart.html')

def checkout(request):
    return render(request,'checkout.html')

def shop(request):
    return render(request,'shop/shop.html')

def wishlist(request):
    return render(request,'wishlist.html')

def login(request):
    return  render(request,"login.html")

def registration(request):
    return  render(request,"registration.html")














