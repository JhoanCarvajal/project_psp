from django.db import models

# Create your models here.

class TimeLog(models.Model):
    program_id = models.ForeignKey("programs.Program", verbose_name="Programa", on_delete=models.CASCADE)
    phase_id = models.ForeignKey("phases.Phase", verbose_name="Fase", on_delete=models.CASCADE)
    startDate = models.DateTimeField(verbose_name="Fecha y hora de inicio", auto_now_add=True)
    interruption = models.IntegerField(verbose_name="Interrupciones", null=True, blank=True)
    stopDate = models.DateTimeField(verbose_name="Fecha y hora de fin", null=True, blank=True)
    delta = models.IntegerField(verbose_name="Tiempo min", null=True, blank=True)
    description = models.TextField(verbose_name="Descripción", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Registro de tiempo"
        verbose_name_plural = "Registro de tiempos"
        ordering = ['startDate']

    def __str__(self):
        return self.description