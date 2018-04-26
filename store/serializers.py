from rest_framework import serializers
from store.models import Store, Transporter
from customers.serializers import UserSerializer


class TransporterSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Transporter
        fields = ('id', 'created', 'address', 'store', 'user', 'active')


class StoreSerializer(serializers.ModelSerializer):
    transporters = TransporterSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Store
        fields = ('id', 'created', 'name', 'address', 'user', 'active', 'transporters')