from django.shortcuts import render
from .models import PartesReusada
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import slugify
from partesGenerales.models import PartesGeneral
from programas.models import Programa
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class PartesReusadaCreateView(CreateView):
    model = PartesReusada
    fields = ['id_programa','id_parte_general','plan','actual']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["programa"] = Programa.objects.get(id=self.kwargs.get('pk'))
        context["partes_generales"] = PartesGeneral.objects.all()
        return context
    
    
    def get_success_url(self):
        nombre = slugify(self.object.id_programa.nombre)
        return reverse_lazy('detalles_programa', args=[self.object.id_programa.id, nombre])
