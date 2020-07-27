from programas.models import Programa
from .models import Lenguaje, Medida

def get_programasDeUsuario(request):
    programas= Programa.objects.all()
    return {'lista_programas':programas}

def get_lenguajes(request):
    lenguajes = Lenguaje.objects.all() 
    return {'lista_lenguajes':lenguajes}

def get_medidas(request):
    medidas = Medida.objects.all() 
    return {'lista_medidas':medidas}
