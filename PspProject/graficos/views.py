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
#funciones
from .funciones.resumen_tiempos import matrizResumenTiempos
from .funciones.defectos_en_fase import defectos_en_fase
from .funciones.defectos_removidos_fase import defectos_removidos_fase
# Create your views here.
class GraficosDetailView(DetailView):
    model = Programa
    template_name='graficosPie/grafico1.html'
    def get_context_data(self, **kwargs):
        context = super(GraficosDetailView, self).get_context_data(**kwargs)
        programa = Programa.objects.get(id=self.kwargs.get('pk'))
        psp = programa.id_proyecto.id_proceso.numero
        context["psp"] = psp
        context["programa"] = programa

        fases = Fase.objects.all().order_by('id')
        cantidad_fases = Fase.objects.count()
        tiempos_programa = RegistroTiempo.objects.filter(id_programa__id=self.kwargs.get('pk'))
        context["registro_tiempos_programa"] = tiempos_programa
        defectos_programa = RegistroDefecto.objects.filter(id_programa__id=self.kwargs.get('pk'))
        #para resumen de defectos inyectados en fase
        context["defectos_ingresados"] = defectos_en_fase(defectos_programa, fases, cantidad_fases)
        #para resumen de defectos removidos en fase
        context["defectos_removidos"] = defectos_removidos_fase(defectos_programa, fases, cantidad_fases)
        #para partes reusadas
        context["partes_reusada"]= PartesReusada.objects.filter(id_programa=self.kwargs.get('pk'))
        #partes añadidas
        context["partes_añadida"]= PartesAñadida.objects.filter(id_programa=self.kwargs.get('pk'))
      
        #para resumen de tiempos
        context["datos"], context["total_actual"] = matrizResumenTiempos(tiempos_programa, fases, cantidad_fases)

        if psp >= 1:
            #para resumen de partes base
            context["partesBases"] = PartesBase.objects.filter(id_programa__id=self.kwargs.get('pk'))
        
        return context