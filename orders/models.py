# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='products', on_delete=models.CASCADE)
    address = models.ForeignKey('address.Address', related_name='address', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_no = models.CharField(blank=False,max_length=100)
    total_price = models.DecimalField(decimal_places=0,max_digits=6)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
