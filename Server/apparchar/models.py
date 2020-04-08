from django.db import models
from django.contrib.auth.models import AbstractUser
#este van a ser mis modelos

class User(AbstractUser):

    NIT=models.CharField(max_length=150,blank=True,null=True)
    direccion=models.CharField(max_length=150,blank=True,null=True)
    telefono=models.CharField(max_length=150,blank=True,null=True)
    USERNAME_FIELD='username'