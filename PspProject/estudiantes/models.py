from django.db import models
from django.conf import settings

# Create your models here.
class Estudiante(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="usuario", on_delete=models.CASCADE)
    rol = models.CharField(max_length=200)
    foto = models.TextField()
    certificacion = models.IntegerField(null=True, blank=True)
    id_profesor = models.ForeignKey("profesores.Profesor", verbose_name="profesor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['id_usuario']

    def __str__(self):
        return self.rol