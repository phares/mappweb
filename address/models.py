# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Address(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    place_address = models.CharField(max_length=100, blank=True, default='')
    place_id = models.CharField(max_length=100, blank=True, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    latlng = models.CharField(max_length=100, blank=True, default='')
    contact = models.CharField(max_length=15, blank=False, default='')
    house_no = models.CharField(max_length=100,default='', blank=False,)
    owner = models.ForeignKey('auth.User', related_name='address', blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(Address, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)
