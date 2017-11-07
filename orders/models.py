# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from mapp.sendsms import send_order_sms

status = (('ACTIVE', 'ACTIVE'), ('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'),
          ('PROCESSING', 'PROCESSING'), ('FAILED', 'FAILED'), ('RECEIVED', 'RECEIVED'))


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', blank=False, on_delete=models.CASCADE)
    address = models.ForeignKey('address.Address', related_name='address', blank=False, on_delete=models.CASCADE)
    fee = models.DecimalField(decimal_places=0,max_digits=6, blank=False,default=0)
    status = models.CharField(choices=status,max_length=20, default='RECEIVED')
    quantity = models.IntegerField(blank=False, default=0)
    store = models.ForeignKey('store.Store', related_name='store', blank=True, default=1)
    transporter = models.ForeignKey('store.Transporter', related_name='transporter', blank=True,default=1)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        send_order_sms()

    def __unicode__(self):
        return str(self.id)


class OrderItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='items', blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', related_name='products', blank=False, on_delete=models.CASCADE)
    order = models.ForeignKey('orders.Order', related_name='items', blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField(decimal_places=0, blank=False, max_digits=6)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        super(OrderItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)
