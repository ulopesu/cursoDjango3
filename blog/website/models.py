from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    activated = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    def __str__(self):
        return self.nome