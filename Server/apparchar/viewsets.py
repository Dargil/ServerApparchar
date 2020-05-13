from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        ruta = request.GET['name']
        try:
            client=boto3.client('s3')
            client.upload_fileobj(photo.get('foto'),'apparchar',ruta+'.jpg')
            return Response({'validate':True},status=status.HTTP_200_OK)
        except Exception as e:
            print("error", e)
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def upload_evento_foto(request):
    if request.method=='POST':
        photo=request.data 
        ruta ='evento/'+photo.get('name')
        try:
            client=boto3.client('s3')
            client.upload_fileobj(photo.get('file'),'apparchar',ruta,ExtraArgs={'ACL': 'public-read'})
            #,ExtraArgs={'ACL': 'public-read'}
            return Response({'validate':True},status=status.HTTP_200_OK)
        except Exception as e:
            print("error", e)
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def new_evento(request):
    if request.method == 'POST':
        nombre_data= request.data['nombre']
        hora_inicio_data= request.data['hora_inicio']
        hora_final_data= request.data['hora_final']
        descripcion_data= request.data['descripcion']
        foto_data= request.data['foto']
        fecha_data= request.data['fecha']
        lugar_data= request.data['lugar']
        categoria_data= request.data['categoria']
        empresa_data= request.data['empresa']
        try:
            empresa_object=User.objects.get(username=empresa_data)
            evento_object=Evento(nombre=nombre_data,hora_inicio=hora_inicio_data,hora_final=hora_final_data,lugar=Lugar.objects.get(direccion=lugar_data),descripcion=descripcion_data,foto=foto_data,fecha=fecha_data)
            evento_object.save()
            evento_empresa=EventoEmpresa(evento=evento_object, empresa=empresa_object)
            evento_empresa.save()
            cat_object=Categoria.objects.get(id=categoria_data)
            evento_categoria=EventoCategoria(evento=evento_object,categoria=cat_object)
            evento_categoria.save()
            return Response({'validate':True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print("error", e)
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        nombre_data= request.GET['nombre']
        return Response({'validate':True}, status=status.HTTP_201_CREATED)



class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class LugarViewSet(viewsets.ModelViewSet):
    queryset= Lugar.objects.select_related()
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
