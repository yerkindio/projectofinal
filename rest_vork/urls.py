from django.urls import path
from rest_vork import views
from rest_vork.viewsLogin import login 

urlpatterns= [
    path('lista_Equipo', views.lista_Equipo, name="lista_Equipo"),
    path('lista_Tecnico/<id>', views.lista_Tecnico, name="lista_Tecnico"),
    path('login',login, name="login")
]