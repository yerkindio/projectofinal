from django.contrib import admin
from django.urls import path
from .views import form_agregar, form_modificar, listar, eliminar, modificar, agregar, inicio, contacto, contactoingresado, crearcuenta, ingresado, iniciosesion, micuenta, notebookingresado, notebooks, pc, pcingresado, recuperarcontra, reparaciones, reparacioningresado

urlpatterns = [
    # CRUD
    path('form_agregar/', form_agregar, name="form_agregar"),
    path('form_modificar/<id>', form_modificar, name='form_modificar'),
    path('listar/', listar, name='listar'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('modificar/', modificar, name='modificar'),
    path('agregar/', agregar, name='agregar'),

    # Otras rutas
    path('', inicio, name='inicio'),
    path('inicio/', inicio, name='inicio'),
    path('contacto/', contacto, name="contacto"),
    path('contactoingresado/', contactoingresado, name="contactoingresado"),
    path('crearcuenta/', crearcuenta, name="crearcuenta"),
    path('ingresado/', ingresado, name="ingresado"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('micuenta/', micuenta, name="micuenta"),
    path('notebookingresado/', notebookingresado, name="notebookingresado"),
    path('notebooks/', notebooks, name="notebooks"),
    path('pc/', pc, name="pc"),
    path('pcingresado/', pcingresado, name="pcingresado"),
    path('recuperarcontra/', recuperarcontra, name="recuperarcontra"),
    path('reparaciones/', reparaciones, name="reparaciones"),
    path('reparacioningresado/', reparacioningresado, name="reparacioningresado"),
]