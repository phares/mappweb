from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product


class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', 'products')