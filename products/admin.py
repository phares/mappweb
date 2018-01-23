# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Product, ProductCategory, Display
from django.contrib import admin


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["created", "name", "active", "volume", "category", "image"]
    list_filter = ["active", "category"]
    list_editable = []
    search_fields = ["name", "category"]

    class Meta:
        model = Product
        

admin.site.register(Product, ProductModelAdmin)


class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["created", "name", "active", "image"]
    list_filter = ["name"]
    list_editable = ["name"]
    search_fields = ["name"]

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryModelAdmin)


class DisplayModelAdmin(admin.ModelAdmin):
    list_display = ["created", "name", "active", "image"]
    list_filter = ['name']
    list_editable = ["image"]
    search_fields = ["name"]

    class Meta:
        model = Display


admin.site.register(Display, DisplayModelAdmin)
