from django.db.models.signals import m2m_changed, post_save, post_delete, pre_delete
from django.dispatch import receiver

from .models import User, UserFeed, Message


@receiver(m2m_changed, sender=User.follow_users.through)
def update_user_feed(action, instance, **kwargs):
    if action == 'post_add':
        following_list = instance.follow_users.all()
        for user in following_list:
            for msg in user.messages.all():
                if msg.reply_to:
                    is_reply_and_follow = msg.reply_to.author in following_list
                if not msg.reply_to or is_reply_and_follow:
                    UserFeed.objects.update_or_create(owner=instance, message=msg)

    elif action == 'post_remove':
        follow_users = instance.follow_users.all()
        user_feed = UserFeed.objects.filter(owner=instance).all()
        for post in user_feed:
            if post.message.author not in follow_users:
                feed_msg = UserFeed.objects.filter(owner=instance, message=post.message)
                feed_msg.delete()


@receiver(post_save, sender=Message)
def add_message_in_userfeed(instance, **kwargs):
    UserFeed.objects.update_or_create(owner=instance.author, message=instance)
    followers = instance.author.followers.all()
    if followers:
        for follower in followers:
            if not instance.reply_to or \
             instance.reply_to.author in follower.follow_users.all():
                msg = follower.feed.create(owner=follower, message=instance)
                msg.save()
