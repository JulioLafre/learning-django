from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    print('home')
    return HttpResponse('Blog')

def exemplo(request):
    print('exemplo')
    return HttpResponse('Exemplo')