# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Address(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=100, blank=True,default='')
    road = models.CharField(max_length=100, blank=True,default='')
    contact = models.CharField(max_length=15, blank=True,default='')
    house_no = models.CharField(max_length=100,default='')
    owner = ''
    order = ''

    class Meta:
        ordering = ('created',)
