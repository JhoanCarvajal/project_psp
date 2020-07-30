from django.db import models

# Create your models here.
class Pip(models.Model):
    id_estudiante = models.ForeignKey("estudiantes.Estudiante", verbose_name="Estudiante", on_delete=models.CASCADE)
    fecha=models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    descripcion=models.TextField(verbose_name="Descripcion")
    solucion=models.TextField(verbose_name="Solucion")
    comentarios=models.TextField(verbose_name="Comentarios")

    class Meta:
        verbose_name ="Pip"
        verbose_name_plural ="Pips"

    def __str__(self):
        return self.descripcion