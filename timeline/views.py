from rest_framework import viewsets

from . import models
from . import serializers as custom_serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = custom_serializers.UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = custom_serializers.MessageSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = custom_serializers.FeedSerializer
