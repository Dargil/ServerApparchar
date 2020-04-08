from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import cliente
from .serializer import ClienteSerializer


@api_view(['GET', 'POST'])
def clienteReq(request):

    if request.method == 'GET':
        clientes=cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        #user = User.objects.get(pk=1).only('id', 'username')
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
