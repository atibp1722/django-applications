from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'assistant_app/index.html')


# def named(request):
#     return HttpResponse('Named URL')


# def numbers(request,id):
#     return HttpResponse(id)