from django.urls import path

from .viewsets import clienteReq

urlpatterns = [
    path('cliente/', clienteReq),
]