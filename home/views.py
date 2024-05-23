from django.shortcuts import render


def home(request):
    print('home')
    
    context = {
            'text': 'Olá home',
            'title': 'Testando dinamismo'
        }
    
    return render(
        request,
        'home/index.html',
        context
    )