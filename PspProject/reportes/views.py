from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Reporte
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy



class ReporteListView(ListView):
    model = Reporte

class ReporteCreateView(CreateView):
    model = Reporte
    fields = ['id_programa','nombre','objetivos','condiciones','resultados_esperados','numero_test','resultados_actules','descripcion']
    success_url = reverse_lazy('lista_reportes')

    
                          
                            
                           
                 
    
