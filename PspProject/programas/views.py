from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#modelos
from .models import Programa
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
#funciones
from .funciones.resumen_tiempos import matrizResumenTiempos
from .funciones.defectos_en_fase import defectos_en_fase
from .funciones.defectos_removidos_fase import defectos_removidos_fase

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
        #para resumen de tiempos
        context["datos"], context["total_actual"] = matrizResumenTiempos(tiempos_programa, fases, cantidad_fases)

        if psp >= 1:
            #para resumen de partes base
            context["partesBases"] = PartesBase.objects.filter(id_programa__id=self.kwargs.get('pk'))
        
        return context

@method_decorator(login_required, name='dispatch')
class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    success_url = reverse_lazy('proyectos', )
    
    def get_context_data(self, **kwargs):
        context = super(ProgramaCreate, self).get_context_data(**kwargs)
        context["id_p"] = Proyecto.objects.get(id=self.kwargs.get('id_p'))
        context["id_u"] = User.objects.get(id=self.kwargs.get('id_u'))
        return context
