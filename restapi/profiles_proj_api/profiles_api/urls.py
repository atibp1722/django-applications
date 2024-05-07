from django.urls import path
from profiles_api import views


urlpatterns=[
    path('base-view/',views.BaseAPIView.as_view(),name='base'),
] 

