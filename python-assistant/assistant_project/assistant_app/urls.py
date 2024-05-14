from django.urls import path
from . import views


urlpatterns=[
    # RETURN DEFAULT PAGE
    path('',views.index,name='index'),

    path('getResponse',views.getResponse,name='getResponse'),
    path('getWeather',views.getWeather,name='getWeather'),
    path('getNews',views.getNews,name='getNews'),
]