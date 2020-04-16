from rest_framework import serializers
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class EventoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoCategoria
        fields = '__all__'
class CategoriaSerializer(serializers.ModelSerializer):
    categoria=EventoCategoriaSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    evento=EventoCategoriaSerializer(many=True,read_only=True)
    class Meta:
        model = Evento
        fields = '__all__'


class EventoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoEmpresa
        fields = '__all__'
