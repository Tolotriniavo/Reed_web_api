from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from .models import Category_Service


class Category_Service_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Category_Service 
        fields = '__all__'
        read_only = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        read_only = ['id']

    def update(self, instance, validated_data):
        u = User.objects.get(pk=instance.id)
        u.set_password(validated_data.get('password'))
        u.username = validated_data.get('username')
        u.save()
        return u