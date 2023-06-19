from django.contrib import admin
from .models import Historiale,Estado,Usuario,Tecnico,Detalle,Equipo,Tipo,Servicio

# Register your models here.

#PERMITE LA ADMINISTRACION DEL MODELO COMPLETO#

admin.site.register(Historiale)
admin.site.register(Estado)
admin.site.register(Usuario)
admin.site.register(Tecnico)
admin.site.register(Detalle)
admin.site.register(Equipo)
admin.site.register(Tipo)
admin.site.register(Servicio)
