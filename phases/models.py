from django.db import models

# Create your models here.
class Phase(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    description = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Fase"
        verbose_name_plural = "Fases"
        ordering = ['name']

    def __str__(self):
        return self.name