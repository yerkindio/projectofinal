from django import forms
from django.forms import ModelForm
from .models import Equipo

class EquipoForm(ModelForm):

    class Meta:
        model= Equipo
        fields= ['id_equipo','id_tipo','id_usuario',
                 'descripcion','sesion','cap_disco','ram','placaM',
                 'procesador','fuente_poder','sistema_op','tipo_disc','gpu']