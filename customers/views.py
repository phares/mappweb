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
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.none()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        elif self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.none()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = permissions.IsAdminUser
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeedbackList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Feedback.objects.all()
        elif self.request.user.is_staff:
            return Feedback.objects.all()
        else:
            return Feedback.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeedbackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Feedback.objects.all()
        elif self.request.user.is_staff:
            return Feedback.objects.all()
        else:
            return Feedback.objects.filter(owner=self.request.user)




