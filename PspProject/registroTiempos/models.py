from django.db import models

# Create your models here.
class RegistroTiempo(models.Model):
    id_fase = models.ForeignKey("mainApp.Fase", verbose_name="Fase", on_delete=models.CASCADE)
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(verbose_name="Fecha de inicio")
    interrupciones = models.IntegerField(verbose_name="Interrupciones", null=True, blank=True)
    fecha_final = models.DateTimeField(verbose_name="Fecha de finalización", null=True, blank=True)
    tiempo_total = models.IntegerField(verbose_name="Timpo tota(Delta)", null=True, blank=True)
    comentarios = models.TextField(verbose_name="Comentarios", null=True, blank=True)
    class Meta:
        verbose_name = "Registro de tiempo"
        verbose_name_plural = "Registro de tiempos"
        ordering = ['fecha_inicio', 'tiempo_total']

    def __str__(self):
        fecha = str(self.fecha_inicio)
        return fecha

    