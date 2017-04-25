# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = ''
    address = ''
    product = ''
    quantity = models.IntegerField(default=0)
    order_no = ''
    total_price =  models.DecimalField(decimal_places=0,max_digits=6)
    type = models.CharField(max_length=100,default='')

    class Meta:
        ordering = ('created',)
