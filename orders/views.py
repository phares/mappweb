# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from orders.serializers import OrderSerializer
from orders.models import Order
from rest_framework import generics,permissions

from django.shortcuts import render

# Create your views here.
class OrdersList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer