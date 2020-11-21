from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='related_comment',
                               on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self',
                               verbose_name='parent comment',
                               null=True,
                               blank=True,
                               related_name='child_comment',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    createdAt = models.DateTimeField(auto_now=True, verbose_name='Created at')

    def __str__(self):
        return f'({self.id}){self.user.username}'

