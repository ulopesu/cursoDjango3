from django.shortcuts import render
from django.contrib import messages
from rest_framework import viewsets

from .models import Post, Contato
from .serializer import ContatoSerializer
from .permissions import contatoPermission

from django.conf import settings


def home(request):
    listaPosts = Post.objects.all()
    data = {
            'posts': listaPosts,
            'site_key': settings.RECAPTCHA_SITE_KEY
            }
    return render(request, 'index.html', data)


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    permission_classes = [contatoPermission]