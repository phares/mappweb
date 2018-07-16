# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals

import urllib

from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order, OrderItem
from rest_framework import generics, permissions, viewsets
from django.shortcuts import render
from mapp.permissions import IsOwnerOrReadOnly
from orders.serializers import OrderStoreSerializer, OrderTasksSerializer


# All Orders
from rest_framework.response import Response


class OrdersList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return Order.objects.all()
        # elif self.request.user.is_staff:
        #     return Order.objects.all()
        # else:
        return Order.objects.filter(owner=self.request.user, clear=False)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(owner=self.request.user)


class OrdersUpdateView(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# End all orders


# All Orders Store
class OrdersStoreList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(store__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersStoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        elif self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(store__user=self.request.user)


# End all orders store


# All Orders Store New
class OrdersStoreReceivedList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.filter(status="RECEIVED")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="RECEIVED")
        else:
            return Order.objects.filter(store__user=self.request.user, status="RECEIVED")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersStoreReceivedDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.filter(status="RECEIVED")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="RECEIVED")
        else:
            return Order.objects.filter(store__user=self.request.user, status="RECEIVED")


# End all orders store New


# All Orders Store Process
class OrdersStoreProcessingList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.filter(status="PROCESSING")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="PROCESSING")
        else:
            return Order.objects.filter(store__user=self.request.user, status="PROCESSING")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersStoreProcessingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.filter(status="PROCESSING")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="PROCESSING")
        else:
            return Order.objects.filter(store__user=self.request.user, status="PROCESSING")


# End all orders store process


# All Orders Store Complete
class OrdersStoreCompleteList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Order.objects.all()
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset
        elif self.request.user.is_staff:
            queryset = Order.objects.all()
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset
        else:
            queryset = Order.objects.filter(store__user=self.request.user)
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersStoreCompleteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Order.objects.all()
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset
        elif self.request.user.is_staff:
            queryset = Order.objects.all()
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset
        else:
            queryset = Order.objects.filter(store__user=self.request.user)
            queryset = queryset.filter(status="COMPLETED") | queryset.filter(status="FAILED") \
                       | queryset.filter(status="CANCELLED")
            return queryset


# End all orders store complete


# Order Item list
class OrdersItemList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# End Order Item list


class OrderTasks(viewsets.ViewSet):
    serializer_class = OrderTasksSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        res = None
        return Response(res)

    def order(self, request, *args, **kwargs):
        order_id = None

        try:
            order_id = request.data.get('order_id')

            # Send sms via url.
            sms_url = 'https://api.africastalking.com/restless/send?username=mapp&' \
                      'Apikey=0be69f64247f7185d4400e15dd631f8035586b0972e58f14c48241e2a47e0ee2&' \
                      'to=+254790331936&message=Order Id.'
            urllib.urlopen(sms_url)

        except Exception as e:
            pass

        return Response(order_id)
