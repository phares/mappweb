# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from address.serializers import AddressSerializer
from address.models import Address
from rest_framework import generics,permissions
from django.shortcuts import render


from mapp.permissions import IsOwnerOrReadOnly


class AddressList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
