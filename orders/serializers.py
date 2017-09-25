from rest_framework import serializers
from orders.models import Order, OrderItem
from address.serializers import AddressSerializer
from products.serializers import ProductSerializer


# Normal class serializer
# ModelSerializer class


class OrderItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'owner', 'product', 'order', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(many=False, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = ('id', 'owner', 'address', 'fee', 'status', 'items')


