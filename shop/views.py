from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/index.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/product_detail.html', context)