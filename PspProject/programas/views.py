from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Programa
from django.contrib.auth.models import User
from .forms import ProgramaForm
from proyectos.models import Proyecto
from mainApp.models import Lenguaje, Medida, Fase
from registroDefectos.models import RegistroDefecto
from registroTiempos.models import RegistroTiempo

from django.db.models import Sum
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy


# Create your views here.
@login_required(login_url='login')
def programa(request):
    return render(request,'programaT/programa.html',{
        'title':'Programa'
    })


def programas(request):
    return render(request,'programaT/programas.html',{
        'title':'Programas'
    })

class ProgramaListView(ListView):
    model = Programa 
    def get_context_data(self, **kwargs):
        context = super(ProgramaListView, self).get_context_data(**kwargs)
        context["programas"] = Programa.objects.filter(id_usuario=self.kwargs.get('id_u'), id_proyecto=self.kwargs.get('id_p'))
        context["id_p"] = Proyecto.objects.get(id=self.kwargs.get('id_p'))
        context["id_u"] = User.objects.get(id=self.kwargs.get('id_u'))
        return context

class ProgramaDetailView(DetailView):
    model = Programa

    def get_context_data(self, **kwargs):
        context = super(ProgramaDetailView, self).get_context_data(**kwargs)
        context["defectos"] = RegistroDefecto.objects.filter(id_programa=self.kwargs.get('pk'))
        tiempos_programa = RegistroTiempo.objects.filter(id_programa__id=self.kwargs.get('pk'))
        tiempo_total = RegistroTiempo.objects.filter(id_programa__id=self.kwargs.get('pk')).annotate(Sum('tiempo_total'))
        fases = Fase.objects.all()

        cantidad_fases = Fase.objects.count()
        matriz = []
        lista_fases = []
        lista_plan = []
        lista_actual = []
        lista_to_date = []
        lista_porcentaje = []
        print(tiempos_programa)
        
        for fase in fases:
            lista_fases.append(fase.nombre)
            parcial = 0
            for t in tiempos_programa:
                if t.id_fase == fase:
                    parcial += t.tiempo_total
            lista_plan.append("No Aplica")
            lista_actual.append(parcial)
            lista_to_date.append(parcial)
            total = 0
            for tiemp in tiempos_programa:
                if parcial != 0:
                    total += tiemp.tiempo_total
            porcen = 0
            porcentaje_redondeado = 0
            if total != 0:
                porcen = ((parcial / total)*100)
            if porcen != 0:
                porcentaje_redondeado = round(porcen, 2)
            lista_porcentaje.append(porcentaje_redondeado)

        


        for i in range(cantidad_fases):
            fila = []
            fila.append(lista_fases[i])
            fila.append(lista_plan[i])
            fila.append(lista_actual[i])
            fila.append(lista_to_date[i])
            fila.append(lista_porcentaje[i])
            matriz.append(fila)

        context["datos"] = matriz
        return context

class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    success_url = reverse_lazy('proyectos', )
    
    def get_context_data(self, **kwargs):
        context = super(ProgramaCreate, self).get_context_data(**kwargs)
        context["id_p"] = Proyecto.objects.get(id=self.kwargs.get('id_p'))
        context["id_u"] = User.objects.get(id=self.kwargs.get('id_u'))
        return context

    