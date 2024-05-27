from django.shortcuts import render
from . import data

# Create your views here.

def blog(request):

    context = {
        'text': 'Iniciando Blog',
        'posts': data.posts
    }
    
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):

    context = {
            'text': 'Iniciando Exemplo'
        }

    return render(
        request,
        'blog/exemplo.html',
        context
    )