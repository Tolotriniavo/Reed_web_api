from django.db import models

class Category_Service(models.Model):
    name = models.CharField(max_length=150)
    descprition = models.CharField(max_length=1000)
# Create your models here.
