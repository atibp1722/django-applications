from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('specific',views.specific,name='specific'),
    path('meal/<int:meal_id>',views.meal,name='meal')
]