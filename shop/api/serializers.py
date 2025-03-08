from django.contrib.auth.models import User
from rest_framework import serializers
from .models import bro


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Ensure the password is hashed before saving."""
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user


class BroSerializer(serializers.ModelSerializer):
    class Meta:
        model=bro
        fields=['id','title','image_url','author']
        extra_kwargs = {"author":{"read_only":True}}