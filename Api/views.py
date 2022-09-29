from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from datetime import datetime
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Category_Service
from .serializers import Category_Service_Serializer
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.decorators import action

# Create your views here.
class Category_Service_APIView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = Category_Service_Serializer
    queryset = Category_Service.objects.all()