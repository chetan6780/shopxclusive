from django.http import HttpResponse
from django.shortcuts import redirect, render
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


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['desc']
        image = request.FILES['upload']
        product = Product.objects.create(
            name=name, price=price, desc=desc, image=image)
        product.save()
    return render(request, 'shop/add_product.html')


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.desc = request.POST['desc']
        product.image = request.FILES['upload']
        product.save()
        return redirect('/shop/products/')
    context = {
        'product': product
    }
    return render(request, 'shop/update_product.html', context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    if request.method == 'POST':
        product.delete()
        return redirect('/shop/products')

    return render(request, 'shop/delete_product.html', context)
