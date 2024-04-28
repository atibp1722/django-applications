from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index')
    path('particular',views.particular,name='particular')
]