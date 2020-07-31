from django.shortcuts import render
from .models import PartesReusada
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify


# Create your views here.
class PartesReusadaCreateView(CreateView):
    model = PartesReusada
    fields = ['id_programa','id_parte_general','plan','actual']

    
    def get_success_url(self):
        nombre = slugify(self.object.id_programa.nombre)
        return reverse_lazy('detalles_programa', args=[self.object.id_programa.id, nombre])
