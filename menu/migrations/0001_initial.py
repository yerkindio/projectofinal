# Generated by Django 4.2.2 on 2023-06-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='note',
            fields=[
                ('idnote', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del note')),
                ('nombrenote', models.CharField(max_length=50, verbose_name='nombre del note')),
            ],
        ),
        migrations.CreateModel(
            name='pc',
            fields=[
                ('idpc', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del pc')),
                ('nombrepc', models.CharField(max_length=50, verbose_name='nombre del pc')),
            ],
        ),
    ]