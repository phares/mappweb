# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from orders.serializers import OrderSerializer,OrderItemSerializer
from orders.models import Order, OrderItem
from rest_framework import generics,permissions
from django.shortcuts import render
from mapp.permissions import IsOwnerOrReadOnly


class OrdersList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersItemList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer