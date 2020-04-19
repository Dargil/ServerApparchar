from django.urls import path

from .viewsets import clienteReq,fotoPerfilUsuario

urlpatterns = [
    path('cliente/', clienteReq),
    path('cliente/uploadFoto',fotoPerfilUsuario),
]