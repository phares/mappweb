from rest_framework import serializers
from orders.models import Order


# Normal class serializer
# ModelSerializer class
class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Order
        fields = ('id','owner','address','product','quantity','order_no','total_price')
