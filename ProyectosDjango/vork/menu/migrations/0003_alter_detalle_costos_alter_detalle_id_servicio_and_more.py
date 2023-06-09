# Generated by Django 4.2.2 on 2023-06-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_detalle_equipo_estados_historial_servicios_tecnico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='costos',
            field=models.IntegerField(verbose_name='costos'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='id_servicio',
            field=models.IntegerField(verbose_name='id servicio'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='id_st',
            field=models.IntegerField(verbose_name='id_st'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='subtotal',
            field=models.IntegerField(verbose_name='subtotal'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_tipo',
            field=models.IntegerField(verbose_name='id tipo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='id_usuario',
            field=models.IntegerField(verbose_name='id usuario'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='id_estado',
            field=models.IntegerField(verbose_name='id del estado'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='id_st',
            field=models.IntegerField(verbose_name='id st'),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='id_st1',
            field=models.IntegerField(verbose_name='id_st1'),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='id_usuario_t',
            field=models.IntegerField(verbose_name='id_usuario_t'),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='total',
            field=models.IntegerField(verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.IntegerField(verbose_name='id del usuario'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(verbose_name='telefono del usuario'),
        ),
    ]
