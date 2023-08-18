from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models import Count
from django.http.request import HttpRequest
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10
    
@admin.register(Customer)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'contact', 'membership']
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category']
    list_per_page = 10
    

    def stock(self, product):
        if product.inventory > 5:
            return 'In Stock'
        else:
            return 'Low on Stock'

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     inlines=[OrerItemInline]


class CartItemInline(admin.TabularInline):
    model=CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines=[CartItemInline]