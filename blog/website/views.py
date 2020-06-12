from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets

from .models import Post, Contato
from .serializer import ContatoSerializer
from .permissions import contatoPermission


def home(request):
    listaPosts = Post.objects.all()
    data = {
            'posts': listaPosts
            }
    return render(request, 'index.html', data)


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [contatoPermission]


















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

    return render(request, 'index.html', data)"
"""



