# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

brands = (('WHISKY','whisky'),('BEER','beer'))

# Create your models here.
class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=False,default='')
    price = models.DecimalField(decimal_places=0,max_digits=6)
    available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    brand = models.CharField(choices=brands, default='whisky', max_length=100)

    class Meta:
        ordering = ('created',)
