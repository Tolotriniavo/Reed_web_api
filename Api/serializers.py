from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from django.core.mail import send_mail
from django.conf import settings
from .models import Category_Service, Service, Contact, Faq


class Category_Service_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Category_Service 
        fields = '__all__'
        read_only = ['id']


class Service_Serializer(serializers.ModelSerializer):
    class Meta: 
        model = Service 
        fields = '__all__'
        read_only = ['id']


class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only = ['id']

    @transaction.atomic
    def create(self, validated_data):
        contact = Contact.objects.create(**validated_data)
        sender = contact.email
        email_text = "Merci de nous avoir contacter. Nous revenons vers vous bientôt"
        send_mail(subject='Ridee Contact',message=email_text,from_email=settings.EMAIL_HOST_USER,recipient_list=[sender])
        return contact 

    def patch(self, instance, validated_data):
        c = Contact.objects.get(pk=instance.id)
        c.is_Read = validated_data.get('is_Read')
        c.save()
        return c

class Faq_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'
        read_only = ['id']


class User_Serializer(serializers.ModelSerializer):
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