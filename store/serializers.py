from rest_framework import serializers
from orders.models import Order, OrderItem
from address.serializers import AddressSerializer
from products.serializers import ProductSerializer
from address.models import Address
from products.models import Product

from store.models import Store, Transporter


class TransporterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transporter
        fields = ('id', 'created', 'address', 'store', 'user', 'active')


class StoreSerializer(serializers.ModelSerializer):
    transporters = TransporterSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'created', 'name', 'address', 'user', 'active', 'transporters')