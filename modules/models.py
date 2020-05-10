from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    project_id = models.ForeignKey("projects.Project", verbose_name="proyecto", on_delete=models.CASCADE, default=0)
    planned = models.IntegerField(verbose_name="Tiempo planeado", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    finished = models.DateTimeField(verbose_name="Fecha de finalización", null=True, blank=True)

    class Meta:
        verbose_name = "Modulo"
        verbose_name_plural = "Modulos"
        ordering = ['name', 'created']

    def __str__(self):
        return self.name