from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):

    class Meta:
        model = Programa
        fields = ['id_usuario', 'id_proyecto', 'nombre', 'descripcion', 'id_lenguaje', 'id_medida', 'fecha_finalizacion']
        widgets = {
            'id_usuario':forms.Select(attrs={'class':'form-control mb-3'}),
            'id_proyecto':forms.Select(attrs={'class':'form-control mb-3'}),
            'nombre':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'descripcion':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'id_lenguaje':forms.Select(attrs={'class':'form-control mb-3'}),
            'id_medida':forms.Select(attrs={'class':'form-control mb-3'}),
            'fecha_finalizacion':forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'dd/mm/yyyy h:m:s'}),
        }