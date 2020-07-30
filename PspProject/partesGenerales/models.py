from django.db import models

# Create your models here.
class PartesGeneral(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    medida_tamaño = models.CharField(verbose_name="Medida de tamaño", max_length=50)
    tipo_contabilidad = models.CharField(verbose_name="Tipo de contabilidad", max_length=50)
    tipo_parte = models.CharField(verbose_name="Tipo de parte", max_length=50)
    tamaño_actual = models.IntegerField(verbose_name="Tamaño actual")
    nombre_contenedor = models.CharField(verbose_name="Nombre de contenedor", max_length=50)

    class Meta:
        verbose_name = "Parte General"
        verbose_name_plural = "Partes Generales"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre