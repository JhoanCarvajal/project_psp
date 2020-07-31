from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#modelo
from .models import TiposDefecto


#login requiret
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(login_required, name='dispatch')
class TiposDefectoListView(ListView):
    model = TiposDefecto

@method_decorator(login_required, name='dispatch')
class TipoDefectoCreateView(CreateView):
    model = TiposDefecto
    fields = ['nombre','descripcion']
    success_url = reverse_lazy('crear_tipos_defectos')
    
