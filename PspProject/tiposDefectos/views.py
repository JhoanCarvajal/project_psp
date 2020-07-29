from django.shortcuts import render
from django.views.generic.list import ListView
#requerir login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#modelo
from .models import TiposDefecto

# Create your views here.


class TiposDefectoListView(ListView):
    model = TiposDefecto