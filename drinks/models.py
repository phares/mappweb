# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

brands = ('whisky')

# Create your models here.
class drinks(models.model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=False,default='')
    price = models.DecimalField()
    available = models.BooleanField(default=True)
    quantity = models.IntegerFiels()
    brand = models.CharField(choices=brands, default='whisky', max_length=100)

    class Meta:
        ordering = ('created',)
