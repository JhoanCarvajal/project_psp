from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def programa(request):
    return render(request,'programaT/programa.html',{
        'title':'Programa'
    })


def programas(request):
    return render(request,'programaT/programas.html',{
        'title':'Programas'
    })