from rest_framework import serializers
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