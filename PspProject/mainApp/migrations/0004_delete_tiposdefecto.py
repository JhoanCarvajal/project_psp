# Generated by Django 3.0.5 on 2020-07-29 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registroDefectos', '0003_auto_20200729_1510'),
        ('mainApp', '0003_fase_tamañoitem_tiposdefecto_tiposparte'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TiposDefecto',
        ),
    ]