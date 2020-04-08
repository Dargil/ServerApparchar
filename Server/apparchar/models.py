from django.db import models


# Create your models here.

class cliente(models.Model):
    nombre = models.CharField('nombre', max_length=100, blank=False)
    edad = models.IntegerField(null=True)
    correo = models.CharField('correo', max_length=40, blank=False)
    telefono = models.CharField('telefono', max_length=100, blank=False)
    usuario = models.CharField('usuario', max_length=40, blank=False, primary_key=True)
    contrasenia = models.CharField('contrasenia', max_length=100, blank=False)
    foto = models.CharField('foto', max_length=100)


