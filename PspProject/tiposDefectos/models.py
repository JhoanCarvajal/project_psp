from django.db import models

# Create your models here.
class TiposDefecto(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo de defecto"
        verbose_name_plural = "Tipos de defectos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre