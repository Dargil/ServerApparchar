from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import cliente
from .serializer import ClienteSerializer
import json
import boto3
from PIL import Image
from io import BytesIO
import base64


@api_view(['GET', 'POST'])
def clienteReq(request):

    if request.method == 'GET':

        user = request.GET['usuario']
        password=request.GET['contrasenia']

        try:
            usuarioxd = cliente.objects.get(usuario=user, contrasenia=password)
            return Response({'validate': True}, status=status.HTTP_200_OK)
        except:
            return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def fotoPerfilUsuario(request):
    if request.method=='POST':
        photo=request.data
        ruta = request.GET['ruta']
        #try:
         #   client=boto3.client('s3')
          #  client.upload_fileobj(photo, "apparchar", ruta)   
           # return Response(status=status.HTTP_200_OK)
        #except:
         #   return Response({'validate': False}, status=status.HTTP_400_BAD_REQUEST)

        client=boto3.client('s3')
        client.upload_fileobj(photo.get('myfile'), "apparchar", ruta)
        return Response({'validate': True}, status=status.HTTP_200_OK)



