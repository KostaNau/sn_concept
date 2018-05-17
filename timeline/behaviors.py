from django.db import models

from .managers import CustomManager


class Timestampable(models.Model):

    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Titleable(models.Model):

    title = models.CharField(max_length=255, null=True, unique=True)

    class Meta:
        abstract = True


class IsVoidable(models.Model):

    is_void = models.BooleanField(default=False)

    objects = CustomManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.is_void = True
        super(self.__class__, self).save(*args, **kwargs)
