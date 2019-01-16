from rest_framework import serializers
from .models import UserApi


class UserApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApi
        fields = ('name', 'data')
