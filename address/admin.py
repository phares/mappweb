# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Address


class AddressModelAdmin(admin.ModelAdmin):
    list_display = ["place_address", "place_id", "name", "latlng", "contact", "house_no", "owner"]
    list_filter = ["place_address", "name"]
    list_editable = []
    search_fields = []

    class Meta:
        model = Address


admin.site.register(Address, AddressModelAdmin)
