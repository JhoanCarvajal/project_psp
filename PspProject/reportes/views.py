from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Reporte

# Create your views here.


class ReporteListView(ListView):
    model = Reporte
    
