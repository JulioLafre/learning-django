from django.shortcuts import render
from . import data
from typing import Any
from django.http import HttpRequest

# Create your views here.

def blog(request):

    context = {
        #'text': 'Iniciando Blog',
        'posts': data.posts
    }
    
    return render(
        request,
        'blog/index.html',
        context
    )

def post(request:HttpRequest, post_id:int):
    found_post: dict[str, Any] | None = None

    for post in data.posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Exception('Post not exist')

    context = {
        #'text': 'Iniciando Blog',
        'post': found_post,
        'title': found_post['title'] + ' - '
    }
    
    return render(
        request,
        'blog/post.html',
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