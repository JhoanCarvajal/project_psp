# Generated by Django 3.0.5 on 2020-07-29 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_delete_tiposdefecto'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='id_proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Proceso', verbose_name='Proceso'),
        ),
    ]
