from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import cliente
from .serializer import ClienteSerializer
import json
import boto3

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

class EventoListViewset(viewsets.ModelViewSet):
    queryset = Evento.objects.select_related()
    serializer_class = EventoSerializer

class CategoriaListViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class EvCaListViewset(viewsets.ModelViewSet):
    queryset = EventoCategoria.objects.select_related()
    serializer_class = EventoCategoriaSerializer

@api_view(['GET', 'POST'])
def clienteReq(request):

    if request.method == 'GET':

        user = request.GET['usuario']
        password=request.GET['contrasenia']       

        try:
            usuarioxd = cliente.objects.get(usuario=user, contrasenia=password)
            return Response({'validate': True}, status=status.HTTP_200_OK)
        except Exception as e:
            print("error",e)
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'POST'])
def fotoPerfilUsuario(request):
    if request.method=='POST':
        photo=request.data
        
        ruta = request.GET['ruta']
        try:
            client=boto3.client('s3')
            client.upload_fileobj(photo.get('foto'),'apparchar',ruta+'.jpg')
            return Response({'validate':True},status=status.HTTP_200_OK)
        except Exception as e:
            print("error", e)
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)




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

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer


@api_view(['GET', 'POST'])
def calificacionReq(request):
    if request.method == 'POST':
        serializer = CalificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        idEvento = request.GET['evento']
        calificaciones = Calificacion.objects.filter(evento_id=idEvento)
        return Response(calificaciones,status=status.HTTP_201_CREATED)


