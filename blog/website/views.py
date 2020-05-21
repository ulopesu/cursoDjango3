from django.shortcuts import render
from .models import Post


def hello_blog(request):
    listaH = [
        'C',
        'C++',
        'Java',
        'Python',
        'JS',
        'TS',
        'Haskell',
        'Ionic',
        'Django',
    ]

    listaPosts = Post.objects.all()

    data = {'name': 'Curso Django',
            'listaHabilidades': listaH,
            'posts': listaPosts
            }

    return render(request, 'index.html', data)
