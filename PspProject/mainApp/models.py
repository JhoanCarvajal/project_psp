from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lenguaje(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



class Medida(models.Model):
    acronimo = models.CharField(verbose_name="Acronimo", max_length=20)
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Medida"
        verbose_name_plural = "Medidas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Proceso(models.Model):
    acronimo = models.CharField(verbose_name="Acronimo", max_length=20)
    nombre = models.CharField(verbose_name="Nombre", max_length=200)

    class Meta:
        verbose_name = "Proceso"
        verbose_name_plural = "Procesos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

        
class Fase(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


    
class TiposDefecto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de defecto"
        verbose_name_plural = "Tipos de defectos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class TiposParte(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de parte"
        verbose_name_plural = "Tipos de partes"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class TamañoItem(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)

    class Meta:
        verbose_name = "Tamaño de item"
        verbose_name_plural = "Tamaños de items"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre