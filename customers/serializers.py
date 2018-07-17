from rest_framework import serializers
from django.contrib.auth.models import User
from orders.models import Order
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
    # products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_active')

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'],
                    first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class FeedbackSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Feedback
        fields = ('id', 'owner', 'message', 'order')
