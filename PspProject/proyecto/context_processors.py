from proyecto.models import Proyect

def get_proyecto(request):
    proyecto= Proyect.objects.values_list('id','nombre','fase' ,'descripcion', 'fechaInicio')
    return {
        'proyectos':proyecto
    }