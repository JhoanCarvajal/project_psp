# Generated by Django 3.0.5 on 2020-05-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='finished',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de finalización'),
        ),
    ]
