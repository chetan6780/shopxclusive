from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]
