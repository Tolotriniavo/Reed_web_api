from django.urls import path, include
from .views import Category_Service_APIView,User_APIView, Category_Service_Read_APIView,Service_Read_APIView, Service_APIView, Contact_APIView, Contact_Read_APIView, Faq_APIView, Faq_Read_APIView, User_APIView
from rest_framework import routers 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()

router.register('category_service_read', Category_Service_Read_APIView, basename='category_service_read')
router.register('category_service', Category_Service_APIView, basename='category_service')


router.register('service_read', Service_Read_APIView, basename='service_read')
router.register('service', Service_APIView, basename='service')


router.register('contact_read', Contact_Read_APIView, basename='contact_read')
router.register('contact', Contact_APIView, basename='contact')

router.register('faq_read', Faq_Read_APIView, basename='faq_read')
router.register('faq', Faq_APIView, basename='faq')

router.register('user', User_APIView, basename='user')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]