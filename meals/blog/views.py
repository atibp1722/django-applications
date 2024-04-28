from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Test')

def specific(request):
    return HttpResponse('Test 2')

def meal(request,meal_id):
    return HttpResponse(meal_id)