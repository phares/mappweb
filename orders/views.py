# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals

import urllib
# Import the helper gateway class
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from orders.serializers import OrderSerializer, OrderItemSerializer
from orders.models import Order, OrderItem
from rest_framework import generics, permissions, viewsets
from django.shortcuts import render
from mapp.permissions import IsOwnerOrReadOnly
from orders.serializers import OrderStoreSerializer, OrderTasksSerializer
from django.shortcuts import get_object_or_404

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
            order = get_object_or_404(Order, pk=order_id)

            if order:
                message = ''
                cost = order.fee  # delivery fee
                items = OrderItem.objects.filter(order=order)
                for i in items:
                    cost += i.price * i.quantity
                    message += i.product.name + ' ' + str(i.quantity) + ' ' + str(i.price) + ', '

                message += 'Delivery ' + str(order.fee) + ' '

                customer_name = order.owner.first_name
                customer_no = order.owner.username
                order_address = order.address.name + ' - ' + order.address.place_address

                if customer_no:
                    try:
                        transporter_no = order.transporter.user.username
                        transporter_name = order.transporter.user.first_name
                        customer_message = message + transporter_name + ' ' + transporter_no + \
                                           ' (' + order_address + ')' + ' ' + str(cost) + '/= '
                        send_sms(customer_no, customer_message)
                    except:
                        pass

                if order.store.active and order.store.user.is_active:
                    try:
                        store_message = message + customer_name + ' ' + customer_no + \
                                        ' (' + order_address + ')' + ' ' + str(cost) + '/= '
                        store_no = order.store.user.username
                        send_sms(store_no, store_message)
                    except:
                        pass

                if order.transporter.active and order.transporter.user.is_active:
                    try:
                        transporter_message = message + customer_name + ' ' + customer_no + \
                                              ' (' + order_address + ')' + ' ' + str(cost) + '/= '
                        transporter_no = order.transporter.user.username
                        send_sms(transporter_no, transporter_message)
                    except:
                        pass

            else:
                print 'No order found'

        except Exception as e:
            print e

        return Response(order_id)


def send_sms(to, message):
    try:
        username = "mapp"
        apikey = "0be69f64247f7185d4400e15dd631f8035586b0972e58f14c48241e2a47e0ee2"
        print to
        print message
        gateway = AfricasTalkingGateway(username, apikey)
        results = gateway.sendMessage(to, message)
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)
