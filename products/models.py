# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

types = (('DRINK','drink'),('VEGETABLE','vegetable'))


# Create your models here.
class ProductCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=types, default='drink', max_length=100)
    name = models.CharField(max_length=100, blank=False,default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', default='/images/default.jpg')


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False,default='')
    price = models.DecimalField(decimal_places=0,max_digits=6)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey('products.ProductCategory', related_name='categories', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)