from rest_framework import serializers
from orders.models import Order


# Normal class serializer
# ModelSerializer class
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','name','price','available','quantity','brand')
