from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('products/', views.products,name='products'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/update/<int:product_id>/', views.update_product, name='update_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/mylistings', views.my_listings,name='my_listings'),

]
