# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import generics,permissions
from mapp.permissions import IsOwnerOrReadOnly
from store.models import Store
from store.models import Transporter

from mapp.permissions import IsOwnerOrReadOnly
from store.serializers import TransporterSerializer, StoreSerializer


class StoreList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StoreSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Store.objects.all()
        elif self.request.user.is_staff:
            return Store.objects.all()
        else:
            return Store.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class TransporterList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Transporter.objects.all()
    serializer_class = TransporterSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TransporterDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Transporter.objects.all()
    serializer_class = TransporterSerializer
