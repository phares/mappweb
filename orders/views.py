# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from orders.serializers import OrdersSerializer
from orders.models import Orders
from rest_framework import generics

from django.shortcuts import render

# Create your views here.
class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer