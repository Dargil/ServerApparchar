from rest_framework import routers
from .views import viewsets
from django.urls import path
from .views import *
routers=routers.SimpleRouter()
routers.register('evento',EventoListViewset)
routers.register('categoria',CategoriaListViewset)
routers.register('eventocategoria',EvCaListViewset)
urlpatterns = routers.urls
