from rest_framework import serializers
from products.models import Product, types, ProductCategory
from django.contrib.auth.models import User

# Normal class serializer
'''
class DrinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True,allow_blank=False,max_length=20)
    price = serializers.DecimalField(decimal_places=0,max_digits=6)
    available = serializers.BooleanField(default=True)
    quantity = serializers.IntegerField(allow_null=True)
    brand = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `DRINK` instance, given the validated data.
        """
        return Drink.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.name)
        instance.price = validated_data.get('code', instance.price)
        instance.availability = validated_data.get('linenos', instance.availability)
        instance.quantity = validated_data.get('language', instance.quantity)
        instance.brand = validated_data.get('style', instance.brand)
        instance.save()
        return instance
'''

# ModelSerializer class
class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ('id','name','price','quantity','category','owner','active')


# ModelSerializer class
class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'type', 'name', 'owner', 'active')