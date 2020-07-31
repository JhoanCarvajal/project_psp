from django.shortcuts import render
from django.urls import reverse, reverse_lazy

#ccbv
from django.views.generic.edit import CreateView

#modelo
from .models import PartesBase

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# Create your views here.
@method_decorator(login_required, name='dispatch')
class ParteBaseCreate(CreateView):
    model = PartesBase
    fields = ['id_programa','id_parte_general','baseplan','planDel','planMod','planAdd','actualBase','actualDel','actualMod','actualAdd']
    success_url = reverse_lazy('proyectos')
