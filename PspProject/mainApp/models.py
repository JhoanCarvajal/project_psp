from django.db import models

# Create your models here.

class Lenguaje(models.Model):
    nombre=models.CharField(max_length=50)

    class Meta:
        verbose_name ="lenguaje"
        verbose_name_plural ="lenguajes"

    def __str__(self):
        return self.nombre



class Medida(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()

    class Meta:
        verbose_name ="Medida de tamaño"
        verbose_name_plural ="Medidas de tamaño"
    
    def __str__(self):
        return self.nombre

    