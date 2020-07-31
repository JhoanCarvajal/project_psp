from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import PartesAñadida
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
#your views here.
@method_decorator(login_required, name='dispatch')
class PartesAñadidaCreate(CreateView):
    model = PartesAñadida
    fields = ['id_programa','nombre','id_tipo_parte','items_planeados','id_tamaño_items','tamaño_planeado','items_acuales','tamaño_actual']
    success_url=reverse_lazy('proyectos')
