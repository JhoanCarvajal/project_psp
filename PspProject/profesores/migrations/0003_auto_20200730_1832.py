# Generated by Django 3.0.5 on 2020-07-30 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0002_auto_20200730_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='rol',
        ),
        migrations.AddField(
            model_name='profesor',
            name='biografia',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Biografia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='contacto',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Contacto'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesor',
            name='foto',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='Foto'),
            preserve_default=False,
        ),
    ]