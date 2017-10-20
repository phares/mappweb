from rest_framework import serializers
from orders.models import Order, OrderItem
from address.serializers import AddressSerializer
from products.serializers import ProductSerializer
from address.models import Address
from products.models import Product

from store.serializers import TransporterSerializer
from store.serializers import StoreSerializer

from store.models import Store, Transporter


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
    transporter = TransporterSerializer(many=False, read_only=True)
    store = StoreSerializer(many=False, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_first_name = serializers.ReadOnlyField(source='owner.first_name')
    owner_last_name = serializers.ReadOnlyField(source='owner.last_name')
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source='address', write_only=True)
    store_id = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(), source='store', write_only=True)
    transporter_id = serializers.PrimaryKeyRelatedField(
        queryset=Transporter.objects.all(), source='transporter', write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'created', 'quantity', 'address', 'address_id', 'owner', 'owner_first_name',
                  'owner_last_name', 'fee', 'status', 'store', 'transporter', 'items', 'store_id', 'transporter_id')


class OrderStoreSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    address = AddressSerializer(many=False, read_only=True)
    transporter = TransporterSerializer(many=False, read_only=True)
    store = StoreSerializer(many=False, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_first_name = serializers.ReadOnlyField(source='owner.first_name')
    owner_last_name = serializers.ReadOnlyField(source='owner.last_name')
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(), source='address', write_only=True)
    store_id = serializers.PrimaryKeyRelatedField(
        queryset=Store.objects.all(), source='store', write_only=True)
    transporter_id = serializers.PrimaryKeyRelatedField(
        queryset=Transporter.objects.all(), source='transporter', write_only=True)

    class Meta:
        model = Order
        fields = ('id', 'created', 'quantity', 'address', 'address_id', 'owner', 'owner_first_name',
                  'owner_last_name', 'fee', 'status', 'store', 'transporter', 'items', 'store_id', 'transporter_id')


