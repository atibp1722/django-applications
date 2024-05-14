from django.urls import path
from . import views


urlpatterns=[
    # RETURN DEFAULT PAGE
    path('',views.index,name='index'),
    # TEST FOR SPECIFICALLY NAMED URL
    path('named_url/',views.named,name='named_url'),
    # TEST FOR NUMBER PASSED IN THE URL 
    path('number/<int:id>',views.numbers,name='number')
]