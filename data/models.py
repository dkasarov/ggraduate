from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import Category
import uuid


class UserApi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    name_url = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    data = models.TextField(default='{}')
    num_of_access = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.pk


class ApiCredentials(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    api = models.ForeignKey(UserApi, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} {self.api.name}'
