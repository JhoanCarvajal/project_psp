# Generated by Django 3.0.5 on 2020-07-30 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_delete_tiposdefecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='numero',
            field=models.IntegerField(default=1, verbose_name='Numero psp'),
            preserve_default=False,
        ),
    ]