from django.db import models

# Create your models here.
class Reporte(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    objetivos = models.TextField(verbose_name="Objetivos")
    condiciones = models.TextField(verbose_name="Condiciones")
    resultados_esperados = models.TextField(verbose_name="Resultados Esperados")
    numero_test = models.IntegerField(verbose_name="Numero de test")
    resultados_actules = models.TextField(verbose_name="Resultados Actules")
    descripcion = models.TextField(verbose_name="Descripción")

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        ordering = ['nombre', 'numero_test']

    def __str__(self):
        return self.nombre