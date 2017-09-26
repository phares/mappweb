from rest_framework import serializers
from orders.models import Order, OrderItem
from address.serializers import AddressSerializer
from products.serializers import ProductSerializer
from address.models import Address
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    product = ProductSerializer(many=False, read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'owner', 'product','product_id', 'order', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(many=False, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source='address', write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'created','address','address_id', 'owner', 'fee', 'status', 'items')


