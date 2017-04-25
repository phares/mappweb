# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from drinks.models import Drink
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drinks.serializers import DrinkSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    """
    List all drinks, or create a new snippet.
    """
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
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