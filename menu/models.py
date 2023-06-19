from django.db import models

# Create your models here.


#modelo para Historial#
class Historiale(models.Model):
    id_historial = models.IntegerField(primary_key=True, verbose_name='id del historial')
    id_estado = models.ForeignKey('Estado', on_delete=models.CASCADE, verbose_name='id del estado')
    id_st = models.IntegerField(verbose_name='id st')
    fecha = models.DateField(max_length=30, verbose_name='fecha')

    def __str__(self):
        return str(self.id_historial)

#modelo para estados#
class Estado(models.Model):
    id_estado = models.IntegerField(primary_key=True, verbose_name='id del estado')
    nombre = models.CharField(max_length=50, verbose_name='nombre')

    def __str__(self):
        return str(self.id_estado)

#modelo para usuarios#
class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='id del usuario')
    nombre = models.CharField(max_length=50, verbose_name='nombre del usuario')
    apellido = models.CharField(max_length=50, verbose_name='apellido del usuario')
    rut = models.IntegerField(verbose_name='id del usuario')
    correo = models.CharField(max_length=50, verbose_name='correo del usuario')
    telefono = models.CharField(max_length=50, verbose_name='telefono del usuario')
    clave = models.CharField(max_length=50, verbose_name='clave del usuario')
    direccion = models.CharField(max_length=50, verbose_name='direccion del usuario')
    id_rol = models.IntegerField(verbose_name='id_rol del usuario')

    def __str__(self):
        return str(self.nombre)

# modelo para tecnico#
class Tecnico(models.Model):
    id_usuario_c = models.OneToOneField('Usuario', on_delete=models.CASCADE, verbose_name='id_usuario_c', primary_key=True, related_name='historiales_asignados')
    f_inicio = models.DateField(verbose_name='fecha inicio')
    f_fin = models.DateField(verbose_name='fecha fin')
    f_entrega = models.DateField(verbose_name='fecha entrega')
    id_usuario_t = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name='id_usuario_t', related_name='historiales_realizados')
    id_st1 = models.IntegerField(verbose_name='id_st1')
    describir_pro = models.TextField(max_length=200, verbose_name='describir')
    diagnostico = models.CharField(max_length=200, verbose_name='diagnostico')
    total = models.CharField(max_length=30, verbose_name='total')

    def __str__(self):
        return str(self.id_usuario_c)

#modelo para detalle#
class Detalle(models.Model):
    id_detalle = models.IntegerField(primary_key=True, verbose_name='id del detalle')
    id_st = models.ForeignKey('Estado', on_delete=models.CASCADE, verbose_name='id_st')
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE, verbose_name='id servicio')
    subtotal = models.CharField(max_length=30, verbose_name='subtotal')
    costos = models.CharField(max_length=30, verbose_name='costos')
    des_costos = models.CharField(max_length=60, verbose_name='descripcion costos')

    def __str__(self):
        return str(self.id_detalle)

#modelo para equipo#
class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True, verbose_name='id equipo')
    id_tipo = models.ForeignKey('Tipo', on_delete=models.CASCADE, verbose_name='id tipo')
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, verbose_name='id usuario')
    descripcion = models.TextField(max_length=200, verbose_name='descripcion equipo')
    sesion = models.CharField(max_length=60, verbose_name='sesion equipo')
    cap_disco = models.CharField(max_length=60, verbose_name='capacidad disco')
    ram = models.CharField(max_length=30, verbose_name='memoria ram')
    placaM = models.CharField(max_length=30, verbose_name='placa madre')
    procesador = models.CharField(max_length=30, verbose_name='procesador')
    fuente_poder = models.CharField(max_length=30, verbose_name='fuente de poder')
    sistema_op = models.CharField(max_length=30, verbose_name='sistema operativo')
    tipo_disc = models.CharField(max_length=30, verbose_name='tipo de disco')
    gpu = models.CharField(max_length=60, verbose_name='tarjeta de video')

    def __str__(self):
        return str(self.id_equipo)

#modelo para tipo#
class Tipo(models.Model):
    id_tipo = models.IntegerField(primary_key=True, verbose_name='id tipo')
    nombre = models.CharField(max_length=60, verbose_name='nombre tipo')

    def __str__(self):
        return str(self.nombre)

#modelo para servicios#
class Servicio(models.Model):
    id_servicio = models.IntegerField(primary_key=True, verbose_name='id servicio')
    nombre = models.CharField(max_length=60, verbose_name='nombre servicio')
    descripcion = models.TextField(max_length=60, verbose_name='descripcion servicio')
    precio = models.CharField(max_length=60, verbose_name='precio servicio')

    def __str__(self):
        return str(self.nombre)