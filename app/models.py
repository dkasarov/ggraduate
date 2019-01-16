from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_pics', default='default.jpg')

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Category(models.Model):
    title = models.CharField(max_length=100)
    new_to_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
