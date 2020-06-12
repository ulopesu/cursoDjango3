from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets

from .models import Post, Contato
from .serializer import ContatoSerializer


def hello_blog(request):
    return render(request, 'index.html')


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer



















"""
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

    return render(request, 'index.html', data)"
"""



