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
from programas.funciones.resumen_tiempos import matrizResumenTiempos
from programas.funciones.defectos_en_fase import defectos_en_fase
from programas.funciones.defectos_removidos_fase import defectos_removidos_fase
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(login_required, name='dispatch')
class GraficosDetailView(TemplateView):
    template_name = "graficosPie/grafico1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fases = Fase.objects.all().order_by('id')
        cantidad_fases = Fase.objects.count()
        tiempos_programa = RegistroTiempo.objects.filter(id_programa__id_usuario__id=self.request.user.id)
        defectos_programa = RegistroDefecto.objects.filter(id_programa__id_usuario__id=self.request.user.id)
        datos, actual = matrizResumenTiempos(tiempos_programa, fases, cantidad_fases)
        defectos_ingresados = defectos_en_fase(defectos_programa, fases, cantidad_fases)

        context["datos"], context["total_actual"] = matrizResumenTiempos(tiempos_programa, fases, cantidad_fases)
        context["defectos_ingresados"] = defectos_en_fase(defectos_programa, fases, cantidad_fases)
        context["defectos_removidos"] = defectos_removidos_fase(defectos_programa, fases, cantidad_fases)

        lista = []
        for d in datos:
            lista.append(d[4])
        context["lista"] = lista

        listaD = []
        for a in defectos_ingresados:
            listaD.append(a[4])
        context["listaD"] = listaD

        return context
    
