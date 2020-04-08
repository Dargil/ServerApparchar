from django.db import models
from django.contrib.auth.models import AbstractUser
#este van a ser mis modelos

class User(AbstractUser):
    age=models.IntegerField(blank=True,null=True,unique=True)
    descripcion=models.CharField(max_length=150,blank=True,null=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['age']