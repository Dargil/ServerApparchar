from django.db import models
from django.contrib.auth.models import AbstractUser
#este van a ser mis modelos

class cliente(models.Model):
    nombre = models.CharField('nombre', max_length=100)
    edad = models.IntegerField(null=True)
    correo = models.CharField('correo', max_length=40)
    telefono = models.CharField('telefono', max_length=100)
    usuario = models.CharField('usuario', max_length=40, primary_key=True)
    contrasenia = models.CharField('contrasenia', max_length=100)
    foto = models.CharField('foto', max_length=100, null=True)

class User(AbstractUser):
    NIT=models.CharField(max_length=150,blank=True,null=True)
    direccion=models.CharField(max_length=150,blank=True,null=True)
    telefono=models.CharField(max_length=150,blank=True,null=True)
    USERNAME_FIELD='username'

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
    hora_inicio =models.TimeField()
    hora_final =models.TimeField()
    lugar  = models.ForeignKey(Lugar, related_name='lugar',on_delete=models.CASCADE)
    descripcion =models.CharField(max_length=255,blank=True,null=True)
    foto  =models.CharField(max_length=255,blank=True,null=True) 
    fecha =models.DateField()

class EventoCategoria(models.Model):
    evento=models.ForeignKey(Evento,related_name='evento',on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,related_name="categoria", on_delete=models.CASCADE)


class EventoEmpresa(models.Model):
    evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    empresa=models.ForeignKey(User,on_delete=models.CASCADE)

class Calificacion(models.Model):
    porcentaje=models.FloatField(null=True)
    comentario=models.CharField(max_length=100, blank=True,null=True)
    multimedia=models.CharField(max_length=100, null=True)
    hora=models.TimeField()
    usuariocliente=models.ForeignKey(cliente,on_delete=models.CASCADE)
    evento=models.ForeignKey(Evento,on_delete=models.CASCADE)
    fecha= models.DateField()
