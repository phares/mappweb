# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import urllib

status = (('CANCELLED', 'CANCELLED'), ('COMPLETED', 'COMPLETED'),
          ('PROCESSING', 'PROCESSING'), ('FAILED', 'FAILED'), ('RECEIVED', 'RECEIVED'))


# Create your models here.
class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='orders', blank=False)
    address = models.ForeignKey('address.Address', related_name='address', blank=False)
    fee = models.DecimalField(decimal_places=0, max_digits=6, blank=False, default=0)
    status = models.CharField(choices=status, max_length=20, default='RECEIVED')
    quantity = models.IntegerField(blank=False, default=0)
    store = models.ForeignKey('store.Store', related_name='store', blank=True, default=1)
    transporter = models.ForeignKey('store.Transporter', related_name='transporter', blank=True, default=1)
    clear = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        # Send sms via url.
        sms_url = 'https://api.africastalking.com/restless/send?username=mapp&' \
                  'Apikey=0be69f64247f7185d4400e15dd631f8035586b0972e58f14c48241e2a47e0ee2&' \
                  'to=+254790331936&message=New M Shopping Order Alert.'
        urllib.urlopen(sms_url)

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
