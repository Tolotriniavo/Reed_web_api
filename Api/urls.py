from django.urls import path, include
from .views import Category_Service_APIView
from rest_framework import routers 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

router.register('category_service', Category_Service_APIView, basename='category_service')



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]