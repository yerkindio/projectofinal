from django.urls import path
from rest_vork.views import lista_Equipo, lista_Tecnico

urlpatterns= [
    path('lista_Equipo', lista_Equipo, name="lista_Equipo"),
    path('lista_Tecnico', lista_Tecnico, name="lista_Tecnico"),
]