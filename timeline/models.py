from django.db import models
from django.contrib.auth.models import User as DjangoUser

from .behaviors import Timestampable, IsVoidable


class User(Timestampable, IsVoidable, DjangoUser, models.Model):

    follow_users = models.ManyToManyField('self',
                                         db_table='following',
                                         symmetrical=False,
                                         blank=True)

    class Meta:
        default_related_name = 'followers'

    def __str__(self):
        return self.username


class Message(Timestampable, IsVoidable, models.Model):

    author = models.ForeignKey(User, models.CASCADE, )
    msg_body = models.CharField(max_length=512)
    reply_to = models.ForeignKey('self', models.CASCADE,
                                 related_name='in_reply_to',
                                 blank=True, null=True)

    class Meta:
        default_related_name = 'messages'

    def __str__(self):
        return '{}, Author: {}'.format(self.msg_body, self.author.username)


class UserFeed(Timestampable, IsVoidable, models.Model):

    owner = models.ForeignKey(User, models.CASCADE)
    message = models.ForeignKey(Message, models.CASCADE)

    class Meta:
        default_related_name = 'feed'

    def __str__(self):
        return "Owner feed: {}, message {}".format(
                                                self.owner.username,
                                                self.message)
