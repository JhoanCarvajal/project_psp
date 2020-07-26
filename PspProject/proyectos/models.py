from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    id_proceso = models.ForeignKey("mainApp.Proceso", verbose_name="Proceso", on_delete=models.CASCADE)
    descripcion=models.TextField(verbose_name="Descripcion")
    fechaInicio=models.DateTimeField(auto_now_add=True, verbose_name="fechaCreacion")
    ultimaActualizacion=models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name ="Proyecto"
        verbose_name_plural ="Proyectos"

    def __str__(self):
        return self.nombre