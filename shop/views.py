from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")


def products(request):
    page_obj = products = Product.objects.all()
    product_name = request.GET.get('product_name')
    if product_name != '' and product_name is not None:
        page_obj = products.filter(name__icontains=product_name)
    paginator = Paginator(page_obj, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'shop/index.html', context)

# class bases view
# class ProductListView(ListView):
#     model = Product
#     template_name = 'shop/index.html'
#     context_object_name = 'products'
#     paginate_by = 3


# def product_detail(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product
#     }
#     return render(request, 'shop/product_detail.html', context)

# Class Bases product view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'product'


# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         price = request.POST['price']
#         desc = request.POST['desc']
#         seller_name = request.user
#         image = request.FILES['upload']
#         product = Product.objects.create(
#             name=name, price=price, desc=desc, image=image, seller_name=seller_name)
#         product.save()
#         return redirect('/shop/products/')
#     return render(request, 'shop/add_product.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    # product_form.html : automatically looks for this template


# @login_required
# def update_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     if request.method == 'POST':
#         product.name = request.POST['name']
#         product.price = request.POST['price']
#         product.desc = request.POST['desc']
#         product.image = request.FILES['upload']
#         product.save()
#         return redirect('/shop/products/')
#     context = {
#         'product': product
#     }
#     return render(request, 'shop/update_product.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    # Automatically generates the template but we can customize it like below
    template_name_suffix = '_update_form'
    # now it will look for --> product_update_form.html

# @login_required
# def delete_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     context = {
#         'product': product
#     }
#     if request.method == 'POST':
#         product.delete()
#         return redirect('/shop/products')

#     return render(request, 'shop/delete_product.html', context)


class ProductDeleteView(DeleteView):
    model = Product
    # create <model>_confirm_delete.html
    success_url = reverse_lazy('shop:products')


def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products': products,
    }
    return render(request, 'shop/my_listing.html', context)
