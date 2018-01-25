# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order, OrderItem
from rest_framework import generics, permissions
from django.shortcuts import render
from mapp.permissions import IsOwnerOrReadOnly
from orders.serializers import OrderStoreSerializer


# All Orders


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
    permission_classes = (permissions.IsAuthenticated, )
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
            return Order.objects.filter(status="COMPLETED")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="COMPLETED")
        else:
            return Order.objects.filter(store__user=self.request.user,status="COMPLETED")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrdersStoreCompleteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrderStoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.filter(status="COMPLETED")
        elif self.request.user.is_staff:
            return Order.objects.filter(status="COMPLETED")
        else:
            return Order.objects.filter(store__user=self.request.user, status="COMPLETED")
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
