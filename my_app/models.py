from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):

    class Status(models.TextChoices):
        PB = 'Published', 'Published'
        DR = 'Draft', 'Draft'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.DR)

    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


