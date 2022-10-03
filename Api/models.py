from django.db import models
from datetime import datetime


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class ImageforCKEditor(models.Model):
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

class Category_Service(models.Model):
    name = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150)
    name_fr = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    description_eng = models.CharField(max_length=1000)
    description_fr = models.CharField(max_length=1000)
    couleur = models.CharField(max_length=10)
    #image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Service(models.Model):
    name = models.CharField(max_length=150)
    name_eng = models.CharField(max_length=150)
    name_fr = models.CharField(max_length=150)
    icone_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    banner_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    slogan = models.CharField(max_length=150)
    slogan_eng = models.CharField(max_length=150)
    slogan_fr = models.CharField(max_length=150)
    auteur = models.CharField(max_length=150)
    resume = models.CharField(max_length=1500)
    resume_eng = models.CharField(max_length=1500)
    resume_fr = models.CharField(max_length=1500)
    tag = models.CharField(max_length=150)
    description = models.TextField()
    description_eng = models.TextField()
    description_fr = models.TextField()
    category = models.ForeignKey(Category_Service, null = True, on_delete = models.SET_NULL)


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    description = models.CharField(max_length=10000)
    is_Read = models.BooleanField(default=False, blank=True)


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    question_eng = models.CharField(max_length=500)
    answer_eng = models.CharField(max_length=500)
    question_fr = models.CharField(max_length=500)
    answer_fr = models.CharField(max_length=500)
# Create your models here.


