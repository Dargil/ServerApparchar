from rest_framework import viewsets

from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset= Lugar.objects.all()
    serializer_class = LugarSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset= Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset= Evento.objects.all()
    serializer_class = EventoSerializer

class EventoCategoriaViewSet(viewsets.ModelViewSet):
    queryset= EventoCategoria.objects.all()
    serializer_class = EventoCategoriaSerializer

class EventoEmpresaViewSet(viewsets.ModelViewSet):
    queryset= EventoEmpresa.objects.all()
    serializer_class = EventoEmpresaSerializer