from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    meal='chicken'
    response=requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+meal+"&app_id=35339e85&app_key=1da925c3ec3e865c20c5fe6db3e3f8c5")
    json_response=response.json()
    meals=json_response['hits']
    return render(request,'blog/index.html',{'meals':meals})

def specific(request):
    return HttpResponse('Test 2')
