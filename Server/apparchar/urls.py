from rest_framework import routers

from .viewsets import *

router=routers.SimpleRouter()
router.register('users',UserViewSet)
router.register('lugar',LugarViewSet)
router.register('categoria',CategoriaViewSet)
router.register('evento',EventoViewSet)
router.register('eventocategoria',EventoCategoriaViewSet)
router.register('eventoempresa',EventoEmpresaViewSet)

urlpatterns=router.urls