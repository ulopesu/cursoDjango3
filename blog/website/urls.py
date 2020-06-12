from django.urls import path, include
from .views import hello_blog, ContatoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('contatos', ContatoViewSet)

urlpatterns = [
    path('blog/', hello_blog, name='hello_blog'),
]

urlpatterns += router.urls