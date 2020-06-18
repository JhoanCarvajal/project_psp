from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def modulos(request):
    return render(request, 'mainApp/modulos.html',{
        'title':'Modulos'
    })
    
@login_required(login_url='login')
def proyectos(request):
    return render(request, 'mainApp/proyectos.html',{
        'title':'Proyectos'
    })