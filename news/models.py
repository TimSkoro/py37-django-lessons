import uuid

from django.contrib.auth.models import User
from django.db import models
from time import time
from slugify import slugify


class Comment(models.Model):
    text = models.TextField()
    news = models.ForeignKey('News', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=200, verbose_name='NASVANNE', help_text='200 letters',
                             unique_for_month="published_at")
    description = models.TextField(max_length=2000)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    changed_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    timestamp = models.FloatField(default=0, editable=False)

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'Novost'
        ordering = ['-published_at', 'pk']
        get_latest_by = 'published_at'


    @property
    def published(self):
        return bool(self.published_at)

    def save(self, *a, **kw):
        if not self.pk:  # pk = ID
            self.timestamp = time()
        return super().save(*a, **kw)

    def __str__(self):
        return self.title
