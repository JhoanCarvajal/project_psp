from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from programas.models import Programa
from django.views import generic
from django.http import HttpResponse


# Create your views here.
def inicio(request):
    return redirect('login')

@login_required(login_url='login')
def modulos(request):
    return render(request, 'mainApp/modulos.html',{
        'title':'Modulos'
    })
    
@login_required(login_url='login')
def proyectos(request):
    if request.method == 'POST':
        nombre=request.POST['nombre']
        return HttpResponse(nombre)
    else:
        return render(request, 'mainApp/proyectos.html',{
            'title':'Proyectos'
        })
        

@login_required(login_url='login')
def programasDeUsuarios(request, id_proyecto):
    return render(request,'mainApp/lista_programas.html', {'id_pro':id_proyecto, 'title':'programas de usuario'})
