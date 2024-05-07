from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views


router=DefaultRouter()
router.register('base-viewset',views.BaseViewSet,basename='base-viewset')
router.register('profile',views.UserProfileViewSet,basename='profile-viewset')

urlpatterns=[
    path('base-view/',views.BaseAPIView.as_view(),name='base'),
    path('login/',views.UserLoginAPIView.as_view(),name='login'),
    path('',include(router.urls)),
] 
