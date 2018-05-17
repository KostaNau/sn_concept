from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('id', 'username', 'follow_users', )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Message
        fields = ('id', 'author', 'msg_body', 'reply_to')


class FeedContentSerializer(serializers.ModelSerializer):

    author = serializers.CharField(source='message.author')
    msg_content = serializers.CharField(source='message.msg_body')
    in_reply_to = serializers.CharField(source='message.reply_to')

    class Meta:
        model = models.UserFeed
        fields = ('author', 'msg_content', 'in_reply_to', )


class FeedSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='owner.username')
    feed = FeedContentSerializer(many=True)

    class Meta:
        model = models.User
        fields = ('username', 'feed', )
