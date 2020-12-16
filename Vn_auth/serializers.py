from rest_framework import serializers
from django.contrib.auth import get_user_model as User
from .models import Notes


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        extra_kwargs = {'user': {'read_only': True}}
        fields = '__all__'