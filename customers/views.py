from django.contrib.auth.models import User
from rest_framework import generics,viewsets,permissions
from customers.serializers import UserSerializer
from customers.serializers import FeedbackSerializer
from customers.models import Feedback


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeedbackList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

