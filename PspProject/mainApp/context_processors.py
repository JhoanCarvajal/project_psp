from programas.models import Programa

def get_programasDeUsuario(request):
    programas= Programa.objects.all()
    
    return {
        'lista_programas':programas
    }