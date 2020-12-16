from rest_framework import serializers
from django.contrib.auth import get_user_model as User
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        extra_kwargs = {'user': {'read_only': True}}
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        extra_kwargs = {'password': {'write_only': True}}
        fields = ["id", "email", "password"]