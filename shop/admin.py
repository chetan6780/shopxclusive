import imp
from unicodedata import name
from django.contrib import admin
from .models import Product


admin.site.site_header = 'Shopxclusive'
admin.site.site_title = 'Shopxclusive'
# admin.site.index_title = 'Manage ABC buying website'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'desc', 'image', 'seller_name')
    search_fields = ('name',)
    actions = ('set_price_to_zero',)
    list_editable = ('price', 'desc')

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)


admin.site.register(Product, ProductAdmin)
