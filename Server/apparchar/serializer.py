from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['NIT', 'first_name', 'last_name', 'email',
                  'direccion', 'telefono', 'username', 'password', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = '__all__'

class EventoEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoEmpresa
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