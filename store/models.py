# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, unique=True, blank=False, default='No Name')
    owner = models.ForeignKey('auth.User', related_name='store', blank=False)
    address = models.ForeignKey('address.Address', related_name='store_address', blank=False)
    user = models.OneToOneField(User, unique=True, related_name='store_user', blank=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Store, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)


class Transporter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='transporter', blank=False)
    address = models.ForeignKey('address.Address', related_name='transporter_address', blank=False)
    store = models.ForeignKey('store.Store', related_name='transporters', blank=False)
    user = models.OneToOneField(User, unique=True, related_name='transport_user', blank=False)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Transporter, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)
