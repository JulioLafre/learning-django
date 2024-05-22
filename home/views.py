from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    print('home')
    return HttpResponse('Home1')