from django.contrib import admin
from .models import Usuario,Lugar,Categoria,Evento,EventoCategoria,EventoEmpresa
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Lugar)
admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(EventoCategoria)
admin.site.register(EventoEmpresa)
