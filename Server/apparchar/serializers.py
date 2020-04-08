from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ['NIT','first_name','last_name','email','direccion','telefono', 'username', 'password', ]
            extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user