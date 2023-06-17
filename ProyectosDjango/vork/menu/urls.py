from django.contrib import admin
from django.urls import path, include
from .views import inicio, clientes,contacto,contactoingresado,crearcuenta,index,ingresado,iniciosesion,micuenta,notebookingresado,notebooks,pc,pcingresado,Perfil,recuperarcontra,reparaciones,reparacioningresado

urlpatterns = [
    path('inicio', inicio, name='inicio'),
    path('clientes/',clientes,name="clientes"), 
    path('contacto/',contacto,name="contacto"),
    path('contactoingresado/',contactoingresado,name="contactoingresado"),
    path('crearcuenta/',crearcuenta,name="crearcuenta"),
    path('index/',index, name='index'),
    path('ingresado/',ingresado,name="ingresado"),
    path('iniciosesion/',iniciosesion,name="iniciosesion"),
    path('micuenta/',micuenta,name="micuenta"),
    path('notebookingresado/',notebookingresado,name="notebookingresado"),
    path('notebooks/',notebooks,name="notebooks"),
    path('pc/',pc,name="pc"),
    path('pcingresado/',pcingresado,name="pcingresado"),
    path('Perfil/',Perfil,name="Perfil"),
    path('recuperarcontra/',recuperarcontra,name="recuperarcontra"),
    path('reparaciones',reparaciones,name="reparaciones"),
    path('reparacioningresado',reparacioningresado,name="reparacioningresado"),

]