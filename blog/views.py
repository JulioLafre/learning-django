from django.shortcuts import render

# Create your views here.

def blog(request):
    print('home')
    return render(
        request,
        'blog/index.html'
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )