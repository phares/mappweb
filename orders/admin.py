# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Order, OrderItem


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["created", "owner", "address", "fee", "status", "quantity", "store", "transporter", "clear"]
    list_filter = ["store", "transporter"]
    list_editable = ["status"]
    search_fields = ["owner"]

    class Meta:
        model = Order


admin.site.register(Order, OrderModelAdmin)


class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["created", "owner", "product", "order", "quantity", "price"]
    list_filter = ['order']
    list_editable = []
    search_fields = []

    class Meta:
        model = OrderItem


admin.site.register(OrderItem, OrderItemModelAdmin)
