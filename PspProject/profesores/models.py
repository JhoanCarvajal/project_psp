from django.db import models
from django.conf import settings

# Create your models here.
class Profesor(models.Model):
    rol = models.CharField(max_length=200)
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="usuario", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['id_usuario']

    def __str__(self):
        return self.rol