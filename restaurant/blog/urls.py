from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('particular',views.particular,name='particular'),
    path('menu',views.menu,name='menu'),
    path('specials',views.specials,name='specials'),
    path('meals',views.meals,name='meals')
]