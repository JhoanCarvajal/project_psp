from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Proyecto

# Create your views here.


class ProyectoListView(ListView):
    model = Proyecto