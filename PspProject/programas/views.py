from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Programa
from django.contrib.auth.models import User
from .forms import ProgramaForm
from proyectos.models import Proyecto
from mainApp.models import Lenguaje, Medida
from registroDefectos.models import RegistroDefecto


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

def defectos(request):
    return render(request,'programaT/defectos.html',{
        'title':'Defectos'
    })

def listaDefesctos(request):
    return render(request,'programaT/listaDefectos.html',{
        'title':'Lista de defectos'
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

    