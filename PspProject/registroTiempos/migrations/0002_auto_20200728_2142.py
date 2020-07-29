# Generated by Django 3.0.5 on 2020-07-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroTiempos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrotiempo',
            name='comentarios',
            field=models.TextField(blank=True, null=True, verbose_name='Comentarios'),
        ),
        migrations.AlterField(
            model_name='registrotiempo',
            name='fecha_inicio',
            field=models.DateTimeField(verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='registrotiempo',
            name='interrupciones',
            field=models.IntegerField(blank=True, null=True, verbose_name='Interrupciones'),
        ),
        migrations.AlterField(
            model_name='registrotiempo',
            name='tiempo_total',
            field=models.IntegerField(blank=True, null=True, verbose_name='Timpo tota(Delta)'),
        ),
    ]