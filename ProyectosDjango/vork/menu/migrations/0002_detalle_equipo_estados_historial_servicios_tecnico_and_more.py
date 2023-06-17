# Generated by Django 4.2.2 on 2023-06-16 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del detalle')),
                ('id_st', models.IntegerField(max_length=30, verbose_name='id_st')),
                ('id_servicio', models.IntegerField(max_length=30, verbose_name='id servicio')),
                ('subtotal', models.IntegerField(max_length=30, verbose_name='subtotal')),
                ('costos', models.IntegerField(max_length=30, verbose_name='costos')),
                ('des_costos', models.CharField(max_length=60, verbose_name='descripcion costos')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id_equipo', models.IntegerField(primary_key=True, serialize=False, verbose_name='id equipo')),
                ('id_tipo', models.IntegerField(max_length=30, verbose_name='id tipo')),
                ('id_usuario', models.IntegerField(max_length=30, verbose_name='id usuario')),
                ('descripcion', models.CharField(max_length=200, verbose_name='descripcion equipo')),
                ('sesion', models.CharField(max_length=60, verbose_name='sesion equipo')),
                ('cap_disco', models.CharField(max_length=60, verbose_name='capacidad disco')),
                ('ram', models.CharField(max_length=30, verbose_name='memoria ram')),
                ('placaM', models.CharField(max_length=30, verbose_name='placa madre')),
                ('procesador', models.CharField(max_length=30, verbose_name='procesador')),
                ('fuente_poder', models.CharField(max_length=30, verbose_name='fuente de poder')),
                ('sistema_op', models.CharField(max_length=30, verbose_name='sistema operativo')),
                ('tipo_disc', models.CharField(max_length=30, verbose_name='tipo de disco')),
                ('gpu', models.CharField(max_length=60, verbose_name='tarjeta de video')),
            ],
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del estado')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id_historial', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del historial')),
                ('id_estado', models.IntegerField(max_length=30, verbose_name='id del estado')),
                ('id_st', models.IntegerField(max_length=30, verbose_name='id st')),
                ('fecha', models.DateField(max_length=30, verbose_name='fecha')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id_servicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='id servicio')),
                ('nombre', models.CharField(max_length=60, verbose_name='nombre servicio')),
                ('descripcion', models.CharField(max_length=60, verbose_name='descripcion servicio')),
                ('precio', models.CharField(max_length=60, verbose_name='precio servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id_usuario_c', models.IntegerField(primary_key=True, serialize=False, verbose_name='id_usuario_c')),
                ('f_inicio', models.DateField(max_length=30, verbose_name='fecha inicio')),
                ('f_fin', models.DateField(max_length=30, verbose_name='fecha fin')),
                ('f_entrega', models.DateField(max_length=30, verbose_name='fecha entrega')),
                ('id_usuario_t', models.IntegerField(max_length=30, verbose_name='id_usuario_t')),
                ('id_st1', models.IntegerField(max_length=30, verbose_name='id_st1')),
                ('describir_pro', models.CharField(max_length=200, verbose_name='describir')),
                ('diagnostico', models.CharField(max_length=200, verbose_name='diagnostico')),
                ('total', models.IntegerField(max_length=30, verbose_name='total')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tipo', models.IntegerField(primary_key=True, serialize=False, verbose_name='id tipo')),
                ('nombre', models.CharField(max_length=60, verbose_name='nombre tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del usuario')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre del usuario')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido del usuario')),
                ('rut', models.IntegerField(max_length=50, verbose_name='id del usuario')),
                ('correo', models.CharField(max_length=50, verbose_name='correo del usuario')),
                ('telefono', models.IntegerField(max_length=20, verbose_name='telefono del usuario')),
                ('clave', models.CharField(max_length=50, verbose_name='clave del usuario')),
                ('direccion', models.CharField(max_length=50, verbose_name='direccion del usuario')),
                ('id_rol', models.CharField(max_length=30, verbose_name='id_rol del usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='note',
        ),
        migrations.DeleteModel(
            name='pc',
        ),
    ]