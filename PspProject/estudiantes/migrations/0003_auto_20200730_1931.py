# Generated by Django 3.0.5 on 2020-07-31 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0002_auto_20200730_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='certificacion',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=models.TextField(blank=True, null=True),
        ),
    ]