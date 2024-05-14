from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests


def index(request):
    return render(request,'assistant_app/index.html')


def getResponse(request):
    msg=request.GET.get('userMessage')
    return HttpResponse(msg)


def getWeather(request):
    lat_=str(request.GET.get('lat'))
    long_=str(request.GET.get('long'))
    reqs=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+lat_+"&lon="+long_+"&units=metric&appid=ecd2457b5bc4ae41ec0b12d3cf7f300f")
    json_response=reqs.json()
    name=json_response['name']
    temp=json_response['main']['temp']
    desc=json_response['weather'][0]['description']
    return JsonResponse(json_response)


def getNews(request):
    reqs=requests.get("https://saurav.tech/NewsAPI/everything/cnn.json")
    json_response=reqs.json()
    return JsonResponse(json_response)
