from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .models import Programa
from django.contrib.auth.models import User
from .forms import ProgramaForm


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

class ProgramaCreate(CreateView):
    model = Programa
    form_class = ProgramaForm
    success_url = reverse_lazy('proyectos')

    