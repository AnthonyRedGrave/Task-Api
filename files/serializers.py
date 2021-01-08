from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class FileSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(default = serializers.CurrentUserDefault(), read_only=True)
    id = serializers.ReadOnlyField()
    class Meta:
        model = File
        fields = ('id', 'name', 'user', 'file', 'content',)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
