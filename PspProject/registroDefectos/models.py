from django.db import models

# Create your models here.
class RegistroDefecto(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="Programa", on_delete=models.CASCADE)
    id_tipo_defecto = models.ForeignKey("tiposDefectos.TiposDefecto", verbose_name="Defecto", on_delete=models.CASCADE)
    fecha = models.DateTimeField(verbose_name="Fecha", null=True, blank=True)
    id_fase_creacion = models.ForeignKey("mainApp.Fase", related_name="mainapps_fases_related_creacion", verbose_name="Fase creación", on_delete=models.CASCADE)
    id_fase_eliminacion = models.ForeignKey("mainApp.Fase", related_name="mainapps_fases_related_finalizacion", verbose_name="Fase eliminación", on_delete=models.CASCADE)
    tiempo_arreglo = models.IntegerField(verbose_name="Tiempo duracion de arreglo")

    class Meta:
        verbose_name = "Registro de defecto"
        verbose_name_plural = "Registro de defectos"
        ordering = ['id_tipo_defecto', 'fecha']

    def __str__(self):
        return self.id_programa.nombre