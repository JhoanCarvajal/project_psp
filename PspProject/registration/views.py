from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('proyectos')

    else:
        register_form=RegisterForm()
        if request.method == 'POST':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')
                return redirect('login')
                

        return render(request, 'register/register.html',{
            'register_form' : register_form,
        })
