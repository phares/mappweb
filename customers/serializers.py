from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product
from address.models import Address
from orders.models import Order


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    address = serializers.PrimaryKeyRelatedField(many=True, queryset=Address.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username','email', 'products', 'address', 'orders')