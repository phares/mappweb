# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import Product,ProductCategory
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializer,ProductCategorySerializer
from rest_framework import mixins
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

# Create your views here.
from mapp.permissions import IsOwnerOrReadOnly

'''
@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    """
    List all products, or create a new snippet.
    """
    if request.method == 'GET':
        products = Drink.objects.all()
        serializer = DrinkSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

'''
class DrinkList(APIView):
    """
    List all products, or create a new drink.
    """
    def get(self, request, format=None):
        snippets = Drink.objects.all()
        serializer = DrinkSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DrinkDetail(APIView):
    """
    Retrieve, update or delete a drink instance.
    """
    def get_object(self, pk):
        try:
            return Drink.objects.get(pk=pk)
        except Drink.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        drink = self.get_object(pk)
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        drink = self.get_object(pk)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
class DrinkList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DrinkDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'product categories': reverse('productcategory-list', request=request, format=format),
        'orders': reverse('orders-list', request=request, format=format),
        'Store orders': reverse('ordersstore-list', request=request, format=format),
        'order items': reverse('orderitems-list', request=request, format=format),
        'address': reverse('address-list', request=request, format=format),
        'feedback': reverse('feedback-list', request=request, format=format),
        'stores': reverse('store-list', request=request, format=format),
        'transporters': reverse('transporter-list', request=request, format=format),
    })


class ProductList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCategoryList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer