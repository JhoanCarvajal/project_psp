from django.db import models

# Create your models here.
class RegistroDefecto(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    id_tipo_defecto = models.ForeignKey("mainApp.TiposDefecto", verbose_name="Defecto", on_delete=models.CASCADE)
    fecha_encontrado = models.DateTimeField(verbose_name="Fecha encontrado", null=True, blank=True)
    fecha_removido = models.DateTimeField(verbose_name="Fecha removido", null=True, blank=True)
    id_fase_creacion = models.ForeignKey("mainApp.Fase", verbose_name="Fase creación", on_delete=models.CASCADE)
    id_fase_eliminacion = models.ForeignKey("mainApp.Fase", verbose_name="Fase eliminación", on_delete=models.CASCADE)
    tiempo_arreglo = models.IntegerField(verbose_name="Tiempo duracion de arreglo")

    class Meta:
        verbose_name = "Registro de defecto"
        verbose_name_plural = "Registro de defectos"
        ordering = ['id_tipo_defecto', 'fecha_encontrado']

    def __str__(self):
        return self.fecha_encontrado