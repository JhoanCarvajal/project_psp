from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import PartesAñadida
from django.urls import reverse_lazy

#your views here.
class PartesAñadidaCreate(CreateView):
    model = PartesAñadida
    fields = ['id_programa','nombre','id_tipo_parte','items_planeados','id_tamaño_items','tamaño_planeado','items_acuales','tamaño_actual']
    success_url=reverse_lazy('proyectos')
