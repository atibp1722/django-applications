from django.urls import path
from . import views


urlpatterns=[
    # RETURN DEFAULT PAGE
    path('',views.index,name='index'),

    # TEST FOR SPECIFICALLY NAMED URL
    # path('named_url/',views.named,name='named_url'),

    path('getResponse',views.getResponse,name='getResponse'),
    path('getWeather',views.getWeather,name='getWeather'),
]