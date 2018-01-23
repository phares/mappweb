# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Store, Transporter
from django.contrib import admin


class StoreModelAdmin(admin.ModelAdmin):
    list_display = ["created", "name", "address", "user", "active"]
    list_filter = ["name", "user"]
    list_editable = []
    search_fields = ["name", "user"]

    class Meta:
        model = Store


admin.site.register(Store, StoreModelAdmin)


class TransporterModelAdmin(admin.ModelAdmin):
    list_display = ["created", "address", "store", "user", "active"]
    list_filter = ["user", "store"]
    list_editable = []
    search_fields = ["user", "name"]

    class Meta:
        model = Transporter


admin.site.register(Transporter, TransporterModelAdmin)
