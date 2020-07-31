from django.db import models
from django.conf import settings

# Create your models here.
class Profesor(models.Model):
    foto = models.TextField(verbose_name="Foto")
    biografia = models.TextField(verbose_name="Biografia")
    contacto = models.CharField(verbose_name="Contacto", max_length=50)
    id_usuario = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profesor", verbose_name="usuario", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['id_usuario']

    def __str__(self):
        return self.id_usuario.first_name