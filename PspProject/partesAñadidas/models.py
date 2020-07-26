from django.db import models

# Create your models here.
class PartesAñadida(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    id_tipo_parte = models.ForeignKey("mainApp.TiposParte", verbose_name="Tipo de parte", on_delete=models.CASCADE)
    items_planeados = models.IntegerField(verbose_name="Items planeados")
    id_tamaño_items = models.ForeignKey("mainApp.TamañoItem", verbose_name="Tamaño de items", on_delete=models.CASCADE)
    tamaño_planeado = models.IntegerField(verbose_name="Tamaño planeado")
    items_acuales = models.IntegerField(verbose_name="Items actuales")
    tamaño_actual = models.IntegerField(verbose_name="Tamaño actual")

    class Meta:
        verbose_name = "PartesAñadida"
        verbose_name_plural = "PartesAñadidas"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre