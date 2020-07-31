from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, EstudianteForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from estudiantes.models import Estudiante
from profesores.models import Profesor
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('proyectos')

    else:
        # register_form=RegisterForm()
        # estudiante_form=EstudianteForm()
        # if all((register_form.is_valid(), estudiante_form.is_valid())):
        #     usu = register_form.save()
        #     estu = estudiante_form.save(commit=False)
        #     estu.id_usuario = usu
        #     estu.save()
        #     messages.success(request, 'Te has registrado correctamente')
        #     return redirect('login')
        # # #     estudiante_form.save()
        register_form=RegisterForm()
        estudiante_form=EstudianteForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            estudiante_form = EstudianteForm(request.POST)
            if register_form.is_valid() and estudiante_form.is_valid():
                usuario = register_form.save()
                id_usuario = usuario
                id_profesor = request.POST['id_profesor']
                profesor = Profesor.objects.get(pk=id_profesor)
                estudiante = Estudiante.objects.create(id_usuario=id_usuario, certificacion=False, id_profesor=profesor)
                estudiante.save()
                messages.success(request, 'Te has registrado correctamente')
                return redirect('login')
                

        return render(request, 'register/register.html',{
            'register_form' : register_form,
            'estudiante_form': estudiante_form,
        })

def log_out(request):
    logout(request)
    return redirect ('login')