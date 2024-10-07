from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_at = models.DateField(default=timezone.now)
    author_name = models.CharField(max_length=200)

    class Meta:
        ordering = ['-published_at']