# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from drinks.models import Drink
from drinks.serializers import DrinkSerializer

# Create your views here.
@csrf_exempt
def drink_list(request):
    """
    List all drinks, or create a new drink.
    """
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DrinkSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def drink_detail(request, pk):
    """
    Retrieve, update or delete a drink.
    """
    try:
        drink = Drink.objects.get(pk=pk)
    except Drink.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DrinkSerializer(drink, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        drink.delete()
        return HttpResponse(status=204)