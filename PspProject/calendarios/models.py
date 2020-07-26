from django.db import models

# Create your models here.
class Calendario(models.Model):
    id_programa = models.ForeignKey("programas.Programa", verbose_name="proyecto", on_delete=models.CASCADE)
    fecha_semana = models.DateField(verbose_name="Fecha de semana", auto_now=False, auto_now_add=False)
    horas_acomuladas_actual = models.IntegerField(verbose_name="Horas acomuladas actual")
    horas_acomuladas_plan = models.IntegerField(verbose_name="Horas acomuladas plan")
    horas_actual = models.IntegerField(verbose_name="Horas actual")
    ev_acomuladas_actual = models.CharField(verbose_name="Ev acomuladas actual", max_length=50)
    num_semana = models.IntegerField(verbose_name="Numero de semana")
    ev_pedicted = models.CharField(verbose_name="Ev predicted", max_length=50)
    horas_plan = models.IntegerField(verbose_name="Horas plan")
    ev_acomulativo_predited = models.CharField(verbose_name="Ev acomulativo proyecto", max_length=50)
    pv_acomulados_pla = models.CharField(verbose_name="Pv acomulados plan", max_length=50)
    valor_actual = models.CharField(verbose_name="Valor actual", max_length=50)
    valor_plan = models.CharField(verbose_name="Valor plan", max_length=50)

    class Meta:
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"
        ordering = ['fecha_semana']

    def __str__(self):
        return self.fecha_semana

