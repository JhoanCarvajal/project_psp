from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = models.TextField(verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    finished = models.DateTimeField(verbose_name="Fecha de finalización", null=True, blank=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['name', 'created']

    def __str__(self):
        return self.name