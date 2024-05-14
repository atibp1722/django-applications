from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return render(request,'assistant_app/index.html')


# def named(request):
#     return HttpResponse('Named URL')


def getResponse(request):
    msg=request.GET.get('userMessage')
    return HttpResponse(msg)


def getWeather(request):
    lat_=str(request.GET.get('lat'))
    long_=str(request.GET.get('long'))
    return HttpResponse()