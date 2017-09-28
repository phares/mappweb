from django.contrib.auth.models import User
from rest_framework import generics,viewsets,permissions
from rest_framework import generics,permissions
from customers.serializers import UserSerializer
from customers.serializers import FeedbackSerializer
from customers.models import Feedback
from mapp.permissions import IsOwnerOrReadOnly


# class UserList(generics.ListAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = permissions.IsAdminUser
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeedbackList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer




