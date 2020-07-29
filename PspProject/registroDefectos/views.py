from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#ccb
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#modelos
from programas.models import Programa
from .models import RegistroDefecto
from mainApp.models import Fase
from tiposDefectos.models import TiposDefecto
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def RegistroDefectoCreate(request):
    if request.method=='POST':
        prg = Programa.objects.get(pk=request.POST['id_programa'])
        tipo_defecto = TiposDefecto.objects.get(pk=request.POST['id_tipo_defecto'])
        fase_creacion = Fase.objects.get(pk=request.POST['id_fase_creacion'])
        fase_eliminacion = Fase.objects.get(pk=request.POST['id_fase_eliminacion'])
        rd = RegistroDefecto()
        rd.id_programa = prg
        rd.id_tipo_defecto = tipo_defecto
        rd.fecha = request.POST['fecha']
        rd.id_fase_creacion = fase_creacion
        rd.id_fase_eliminacion = fase_eliminacion
        rd.tiempo_arreglo = request.POST['tiempo_arreglo']
        rd.save()
        slug = slugify(prg.nombre)
    return redirect('/programas/detalles' + '/' + request.POST['id_programa'] + '/' + slug )