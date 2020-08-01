from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#modelos
from .models import Programa 
from partesAñadidas.models import PartesAñadida
from partesReusadas.models import PartesReusada
from django.contrib.auth.models import User
from proyectos.models import Proyecto
from mainApp.models import Lenguaje, Medida, Fase
from registroDefectos.models import RegistroDefecto
from registroTiempos.models import RegistroTiempo
from partesBases.models import PartesBase
#fomulario
from .forms import ProgramaForm
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
from .funciones.estadisticas import timpo_actual, porcentajes, porcentajes_planeados

# Create your views here.
@login_required(login_url='login')
def programa(request):
    return render(request,'programaT/programa.html',{
        'title':'Programa'
    })

@login_required(login_url='login')
def programas(request):
    cont=Programa.objects.all()
    return render(request,'programaT/programas.html',{
        'title':'Programas',
        'contes':cont
    })

@login_required(login_url='login')
def defectos(request):
    return render(request,'programaT/defectos.html',{
        'title':'Defectos'
    })

@login_required(login_url='login')
def listaDefesctos(request):
    return render(request,'programaT/listaDefectos.html',{
        'title':'Lista de defectos'
    })

@method_decorator(login_required, name='dispatch')
class ProgramaListView(ListView):
    model = Programa 
    def get_context_data(self, **kwargs):
        context = super(ProgramaListView, self).get_context_data(**kwargs)
        context["programas"] = Programa.objects.filter(id_usuario=self.kwargs.get('id_u'), id_proyecto=self.kwargs.get('id_p'))
        context["id_p"] = Proyecto.objects.get(id=self.kwargs.get('id_p'))
        context["id_u"] = User.objects.get(id=self.kwargs.get('id_u'))
        return context

@method_decorator(login_required, name='dispatch')
class ProgramaDetailView(DetailView):
    model = Programa

    def get_context_data(self, **kwargs):
        context = super(ProgramaDetailView, self).get_context_data(**kwargs)
        programa = Programa.objects.get(id=self.kwargs.get('pk'))
        psp = programa.id_proyecto.id_proceso.numero

        fases = Fase.objects.all().order_by('id')
        cantidad_fases = Fase.objects.count()
        tiempos_programa = RegistroTiempo.objects.filter(id_programa__id=self.kwargs.get('pk'))
        defectos_programa = RegistroDefecto.objects.filter(id_programa__id=self.kwargs.get('pk'))
        partes_reusada= PartesReusada.objects.filter(id_programa=self.kwargs.get('pk'))
        partes_añadida= PartesAñadida.objects.filter(id_programa=self.kwargs.get('pk'))
        partesBases = PartesBase.objects.filter(id_programa__id=self.kwargs.get('pk'))

        context["psp"] = psp
        context["programa"] = programa
        context["registro_tiempos_programa"] = tiempos_programa
        context["datos"], context["total_actual"] = matrizResumenTiempos(tiempos_programa, fases, cantidad_fases)
        context["defectos_ingresados"] = defectos_en_fase(defectos_programa, fases, cantidad_fases)
        context["defectos_removidos"] = defectos_removidos_fase(defectos_programa, fases, cantidad_fases)
        context["partes_reusada"]= partes_reusada
        context["partes_añadida"]= partes_añadida
        context["partesBases"] = partesBases

        context["tamano_actual"], context["tamano_a"], context["tamano_b"], context["tamano_r"], context["productibidad_actual"], context["tamano_e"] = porcentajes(partes_añadida,partesBases,partes_reusada)
        context["tamano_actual_p"], context["tamano_a_p"], context["tamano_b_p"], context["tamano_r_p"], context["productibidad_actual_p"], context["tamano_e_p"] = porcentajes_planeados(partes_añadida,partesBases,partes_reusada)

        
        return context

@method_decorator(login_required, name='dispatch')
class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    def get_success_url(self):
        return reverse_lazy('lista_programas_usuario', args=[self.object.id_usuario.id, self.object.id_proyecto.id])
    
    def get_context_data(self, **kwargs):
        context = super(ProgramaCreate, self).get_context_data(**kwargs)
        context["id_p"] = Proyecto.objects.get(id=self.kwargs.get('id_p'))
        context["id_u"] = User.objects.get(id=self.kwargs.get('id_u'))
        return context

@method_decorator(login_required, name='dispatch')
class InfoPrograma(TemplateView):
    template_name = "programas/includes/info.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programa'] = Programa.objects.filter(id=self.kwargs.get('pk'))
        return context