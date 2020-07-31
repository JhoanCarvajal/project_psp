from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#ccb
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
#modelos
from programas.models import Programa
from .models import RegistroTiempo
from mainApp.models import Fase

# Create your views here.
class TiemposListView(ListView):
    model = RegistroTiempo
    template_name = "registrotiempos_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = Programa.objects.get(id=self.kwargs.get('pk'))
        return context
    
class RegistroTiempoCreate(CreateView):
    model = RegistroTiempo
    fields = ['id_fase','id_programa', 'fecha_inicio','interrupciones','fecha_final', 'tiempo_total', 'comentarios']

    def get_success_url(self):
        return reverse_lazy('lista_tiempos', args=[self.object.id_programa.id])
    
    def get_context_data(self, **kwargs):
        context = super(RegistroTiempoCreate, self).get_context_data(**kwargs)
        context["programa"] = Programa.objects.get(id=self.kwargs.get('pk'))
        return context

@login_required(login_url='login')
def RegistroTiempoCreatef(request):
    if request.method=='POST':
        prg = Programa.objects.get(pk=request.POST['id_programa'])
        fase = Fase.objects.get(pk=request.POST['id_fase'])
        rt = RegistroTiempo()
        rt.id_fase = fase
        rt.id_programa = prg
        rt.fecha_inicio = request.POST['fecha_inicio']
        if request.POST['interrupciones'] != "":
            rt.interrupciones = request.POST['interrupciones']
        if request.POST['fecha_final'] != "":
            rt.fecha_final = request.POST['fecha_final']
        if request.POST['tiempo_total'] != "":
            rt.tiempo_total = request.POST['tiempo_total']
        if request.POST['comentarios'] != "":
            rt.comentarios = request.POST['comentarios']
        rt.save()