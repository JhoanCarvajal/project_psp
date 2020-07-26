from django.db import models
from django.conf import settings

# Create your models here.
class Programa(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="usuario", on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey("proyectos.Proyecto", verbose_name="proyecto", on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=200)
    descripcion = models.TextField(verbose_name="Descripción")
    id_lenguaje = models.ForeignKey("mainApp.Lenguaje", verbose_name="lenguaje", on_delete=models.CASCADE)
    id_medida = models.ForeignKey("mainApp.Medida", verbose_name="medida", on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    fecha_finalizacion = models.DateTimeField(verbose_name="Fecha de finalización", null=True, blank=True)

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"
        ordering = ['nombre', 'fecha_creacion']

    def __str__(self):
        return self.nombre