from django.db import models

# Create your models here.
class PartesBase(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="Proyecto", on_delete=models.CASCADE)
    id_parte_general = models.ForeignKey("partesGenerales.PartesGeneral", verbose_name="Parte General", on_delete=models.CASCADE)
    baseplan = models.IntegerField(verbose_name="Planeado base")
    planDel = models.IntegerField(verbose_name="Planeado a eliminar")
    planMod = models.IntegerField(verbose_name="Planeado a modificar")
    planAdd = models.IntegerField(verbose_name="Planeado a añadir")
    actualBase = models.IntegerField(verbose_name="Actual base")
    actualDel = models.IntegerField(verbose_name="Actual a eliminar")
    actualMod = models.IntegerField(verbose_name="Actual a modificar")
    actualAdd = models.IntegerField(verbose_name="Actual a añadir")

    class Meta:
        verbose_name = "Parte Base"
        verbose_name_plural = "Partes Bases"
        ordering = ['baseplan']

    def __str__(self):
        return self.baseplan