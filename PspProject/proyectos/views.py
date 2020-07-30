from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Proyecto

#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProyectoListView(ListView):
    model = Proyecto