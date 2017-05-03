from rest_framework import serializers
from orders.models import Order, OrderItem


# Normal class serializer
# ModelSerializer class
class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ('id', 'owner', 'address', 'fee', 'status' )


class OrderItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = OrderItem
        fields = ('id', 'owner', 'product', 'order', 'quantity', 'price')