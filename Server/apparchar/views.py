from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
# Create your views here.
from rest_framework import viewsets
from .serializers import *


class EventoListViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.select_related()
    serializer_class = EventoSerializer

class CategoriaListViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class EvCaListViewset(viewsets.ModelViewSet):
    queryset = EventoCategoria.objects.select_related()
    serializer_class = EventoCategoriaSerializer
