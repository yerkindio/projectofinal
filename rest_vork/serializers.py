from rest_framework import serializers
from menu.models import Equipo,Tecnico

class EquipoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields =['id_equipo','id_tipo','id_usuario','descripcion','sesion','cap_disco','ram','placaM',
                 'procesador','fuente_poder','sistema_op','tipo_disc','gpu']


class TecnicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields =['id_usuario_c','f_inicio','f_fin','f_entrega',
                 'id_usuario_t','id_st1','describir_pro']