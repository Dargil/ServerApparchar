from django.conf.urls import include
from rest_framework import routers
from .viewsets import *
from django.urls import path
from .views import *

router=routers.SimpleRouter()
router.register('users',UserViewSet)
router.register('lugar',LugarViewSet)
router.register('categoria',CategoriaListViewset)
router.register('evento',EventoListViewset)
router.register('eventocategoria',EvCaListViewset)
router.register('eventoempresa',EventoEmpresaViewSet)


urlpatterns = [
    path('cliente/', clienteReq),
    path('cliente/uploadFoto',fotoPerfilUsuario),
    path('', include(router.urls)),
]

