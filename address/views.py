# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from address.serializers import AddressSerializer
from address.models import Address
from rest_framework import generics

from django.shortcuts import render


# Create your views here.
class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
