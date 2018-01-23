# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Order, OrderItem


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["created", "address", "fee", "status", "quantity", "store", "transporter"]
    list_filter = ["store", "transporter"]
    list_editable = ["status"]
    search_fields = ["store", "transporter"]

    class Meta:
        model = Order


admin.site.register(Order, OrderModelAdmin)


class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ["created", "owner", "product", "order", "quantity"]
    list_filter = ['order']
    list_editable = []
    search_fields = ["order"]

    class Meta:
        model = OrderItem


admin.site.register(OrderItem, OrderItemModelAdmin)
