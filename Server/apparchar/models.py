from django.db import models

# Create your models here

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(models.Model):
    NIT=models.CharField(max_length=150,null=True)
    direccion=models.CharField(max_length=150,blank=True,null=True)
    telefono=models.CharField(max_length=150,blank=True,null=True)
    #USERNAME_FIELD='username'

class Lugar(models.Model):
    direccion =models.CharField(max_length=255,blank=True,null=False,primary_key=True)
    nombre =models.CharField(max_length=255,blank=True,null=True)
    coordenada_x =models.FloatField()
    coordenada_y =models.FloatField()
    descripcion =models.CharField(max_length=255,blank=True,null=True)

class Categoria(models.Model):
    nombre =models.CharField(max_length=255,blank=True,null=True)
    icono =models.CharField(max_length=255,blank=True,null=True)


class Evento(models.Model):
    nombre =models.CharField(max_length=255,blank=True,null=True)
    hora_inicio =models.TimeField(auto_now_add=True)
    hora_final =models.TimeField(auto_now_add=True)
    lugar  = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    descripcion =models.CharField(max_length=255,blank=True,null=True)
    foto  =models.CharField(max_length=255,blank=True,null=True)
    fecha =models.DateField(auto_now_add=True)

class EventoCategoria(models.Model):
    evento=models.ForeignKey(Evento,related_name='evento',on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,related_name="categoria", on_delete=models.CASCADE)


class EventoEmpresa(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    empresa=models.ForeignKey(Usuario,on_delete=models.CASCADE)
