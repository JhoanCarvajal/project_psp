# Generated by Django 3.0.5 on 2020-07-25 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0002_proceso'),
        ('proyectos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('id_lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Lenguaje', verbose_name='lenguaje')),
                ('id_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Medida', verbose_name='medida')),
                ('id_proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyecto', verbose_name='proyecto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
                'ordering': ['nombre', 'fecha_creacion'],
            },
        ),
    ]
