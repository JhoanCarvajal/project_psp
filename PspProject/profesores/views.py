from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from .models import Profesor

# Create your views here.

# Create your views here.
@login_required(login_url='login')
def profesorDetalles(request):
    model = Profesor
    return render(request,'profesor/profesorDetalles.html',{'title':'Detalles Profesor'})



    
 
   

    


