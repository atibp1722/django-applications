from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'blog/index.html')

def particular(request):
    return HttpResponse()

def menu(request):
    return render(request,'blog/menu.html')

def specials(request):
    return render(request,'blog/specials.html')

def meals(request):
    return render(request,'blog/meals.html')
 