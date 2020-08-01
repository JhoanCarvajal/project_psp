from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Pip
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from programas.models import Programa


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class PipListView(ListView):
    model = Pip

@method_decorator(login_required, name='dispatch')
class PipCreateView(CreateView):
    model = Pip
    fields = ['id_estudiante','descripcion','solucion','comentarios']
    success_url = reverse_lazy('lista_pips')

    

    
                          
                            
                           
                 
    
