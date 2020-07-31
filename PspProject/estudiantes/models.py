from django.db import models
from django.conf import settings

# Create your models here.
class Estudiante(models.Model):
    id_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="estudiante", verbose_name="usuario", on_delete=models.CASCADE)
    foto = models.TextField(null=True, blank=True)
    certificacion = models.BooleanField(null=True, blank=True)
    id_profesor = models.ForeignKey("profesores.Profesor", related_name="profesor_estudiante", verbose_name="profesor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['id_usuario']

    def __str__(self):
        return self.id_usuario.first_name