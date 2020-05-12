from django.db import models

# Create your models here.
class Program(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    module_id = models.ForeignKey("modules.Module", verbose_name="proyecto", on_delete=models.CASCADE)
    planned = models.IntegerField(verbose_name="Tiempo planeado", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    finished = models.DateTimeField(verbose_name="Fecha de finalización", null=True, blank=True)

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"
        ordering = ['name', 'created']

    def __str__(self):
        return self.name