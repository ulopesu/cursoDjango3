from django.urls import path, include
from .views import home, ContatoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('contatos', ContatoViewSet)

urlpatterns = [
    path('', home, name='home'),
]

urlpatterns += router.urls
