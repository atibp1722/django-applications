from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Home Page Test')


# def named(request):
#     return HttpResponse('Named URL')


# def numbers(request,id):
#     return HttpResponse(id)