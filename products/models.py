# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

types = (('DRINK', 'drink'), ('VEGETABLE', 'vegetable'))


# Create your models here.
class ProductCategory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(choices=types, blank=False, max_length=100)
    name = models.CharField(max_length=100, unique=True, blank=False)
    owner = models.ForeignKey('auth.User', related_name='categories', blank=False, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='categories', blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(ProductCategory, self).save(*args, **kwargs)

    # def __unicode__(self):
    def __str__(self):
        return self.name


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False)
    price = models.DecimalField(decimal_places=0, blank=False, max_digits=6)
    active = models.BooleanField(default=True)
    volume = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    category = models.ForeignKey('products.ProductCategory', blank=False, related_name='products', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='products',blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)


class Display(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False)
    active = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='display')
    image = models.ImageField(upload_to='display', blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Display, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)