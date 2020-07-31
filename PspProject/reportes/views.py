from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Reporte
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from programas.models import Programa


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ReporteListView(ListView):
    model = Reporte

@method_decorator(login_required, name='dispatch')
class ReporteCreateView(CreateView):
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_progr"] = Programa.objects.get(id=self.kwargs.get('pk'))
        return context
    
    model = Reporte
    fields = ['id_programa','nombre','objetivos','condiciones','resultados_esperados','numero_test','resultados_actules','descripcion']
    success_url = reverse_lazy('lista_reportes')
    
                          
                            
                           
                 
    
