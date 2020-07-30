from django.db import models

# Create your models here.
class PartesReusada(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="Programa", on_delete=models.CASCADE)
    id_parte_general = models.ForeignKey("partesGenerales.PartesGeneral", verbose_name="Parte General", on_delete=models.CASCADE)
    plan = models.IntegerField(verbose_name="Tamaño planeado")
    actual = models.IntegerField(verbose_name="Tamaño actual")

    class Meta:
        verbose_name = "Parte Reusada"
        verbose_name_plural = "Partes Reusadas"
        ordering = ['plan']

    def __str__(self):
<<<<<<< HEAD
        d=str(self.plan)
=======
        d = 'parte reusada de '+str(self.id_programa)
>>>>>>> psp3
        return d