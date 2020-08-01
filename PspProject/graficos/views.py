from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#modelos
from programas.models import Programa 
from partesAñadidas.models import PartesAñadida
from partesReusadas.models import PartesReusada
from django.contrib.auth.models import User
from proyectos.models import Proyecto
from mainApp.models import Lenguaje, Medida, Fase
from registroDefectos.models import RegistroDefecto
from registroTiempos.models import RegistroTiempo
from partesBases.models import PartesBase

#para grup by pero
from django.db.models import Sum
#ccb
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
#funciones
from .funciones.resumen_tiempos import matrizResumenTiempos
from .funciones.defectos_en_fase import defectos_en_fase
from .funciones.defectos_removidos_fase import defectos_removidos_fase
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class GraficosDetailView(TemplateView):
    template_name = "graficosPie/grafico1.html"
