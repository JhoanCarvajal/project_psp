from proyectos.models import Proyecto

def get_proyecto(request):
    proyecto= Proyecto.objects.values_list('id','nombre','id_proceso' ,'descripcion', 'fechaInicio')
    
    return {
        'proyectos':proyecto
    }