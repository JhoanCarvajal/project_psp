from programas.models import Programa
from .models import Lenguaje, Medida, Fase, TiposDefecto

def get_programasDeUsuario(request):
    programas= Programa.objects.all()
    return {'lista_programas':programas}

def get_lenguajes(request):
    lenguajes = Lenguaje.objects.all() 
    return {'lista_lenguajes':lenguajes}

def get_medidas(request):
    medidas = Medida.objects.all() 
    return {'lista_medidas':medidas}

def get_fases(request):
    fases = Fase.objects.all() 
    return {'lista_fases':fases}

def get_tiposdefectos(request):
    tipos_defectos = TiposDefecto.objects.all() 
    return {'lista_tipos_defectos':tipos_defectos}

