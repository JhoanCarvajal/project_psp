from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import PartesAñadida
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from programas.models import Programa
from partesGenerales.models import PartesGeneral
from mainApp.models import TamañoItem

# Create your views here.
#your views here.
@method_decorator(login_required, name='dispatch')
class PartesAñadidaCreate(CreateView):
    model = PartesAñadida
    fields = ['id_programa','nombre','id_tipo_parte','items_planeados','id_tamaño_items','tamaño_planeado','items_acuales','tamaño_actual']
    success_url=reverse_lazy('proyectos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programa"] = Programa.objects.get(id=self.kwargs.get('pk'))
        context["partes_generales"] = PartesGeneral.objects.all()
        context["tms"] = TamañoItem.objects.all()
        return context
    
