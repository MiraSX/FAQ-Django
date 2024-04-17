from django.db import models
from django.utils import timezone


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images", default="images/no_image.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved = models.BooleanField(default=False)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
