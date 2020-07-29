from django import forms
from .models import RegistroTiempo

class RegTiemposForm(forms.Form):
    model = RegistroTiempo
    fields = ['id_fase','id_programa','fecha_inicio','interrupciones','fecha_final','tiempo_total','comentarios']