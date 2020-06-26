from django.db import models
from django.contrib.auth.models import User

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


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.CharField(max_length=200, null=True, blank=True)
    rol = models.CharField(max_length=50)
    lenguaje = models.ForeignKey(Lenguaje, on_delete=models.CASCADE)
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE)

    class Meta:
        verbose_name ="Perfil del usuario"
        verbose_name_plural ="Perfiles de usuarios"
    
    def __str__(self):
        return self.user


    