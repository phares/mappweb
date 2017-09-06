from rest_framework import serializers
from django.contrib.auth.models import User
from customers.models import Feedback

'''
class UserSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    address = serializers.PrimaryKeyRelatedField(many=True, queryset=Address.objects.all())
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username','email', 'products', 'address', 'orders')
'''


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'products')


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = ('id', 'owner', 'message')
