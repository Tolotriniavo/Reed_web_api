from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Category_Service, Service, Contact, Faq
from .serializers import User_Serializer, Category_Service_Serializer, Service_Serializer, Contact_Serializer, Faq_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser



# Categorie
class Category_Service_Read_APIView(ReadOnlyModelViewSet):
    serializer_class = Category_Service_Serializer
    queryset = Category_Service.objects.all()

class Category_Service_APIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Category_Service_Serializer
    queryset = Category_Service.objects.all()


# Service
class Service_Read_APIView(ReadOnlyModelViewSet):
    serializer_class = Service_Serializer
    def get_queryset(self):
        queryset = Service.objects.all()
        id = self.request.GET.get('id')
        category = self.request.GET.get('category')
        if id is not None:
            queryset = Service.objects.filter(id=id)
        if category is not None:
            queryset = Service.objects.filter(category=category)
        return queryset

class Service_APIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = Service_Serializer
    def get_queryset(self):
        queryset = Service.objects.all()
        id = self.request.GET.get('id')
        category = self.request.GET.get('category')
        if id is not None:
            queryset = Service.objects.filter(id=id)
        if category is not None:
            queryset = Service.objects.filter(category=category)
        return queryset

#Contact 
class Contact_Read_APIView(ReadOnlyModelViewSet):
    serializer_class = Contact_Serializer
    queryset = Contact.objects.all()

class Contact_APIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Contact_Serializer
    queryset = Contact.objects.all()

#FAQ
class Faq_Read_APIView(ReadOnlyModelViewSet):
    serializer_class = Faq_Serializer
    queryset = Faq.objects.all()

class Faq_APIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Faq_Serializer
    queryset = Faq.objects.all()

#User
class User_APIView(ModelViewSet):
    serializer_class = User_Serializer
    queryset = User.objects.all()    
    permission_classes = [IsAuthenticated]
