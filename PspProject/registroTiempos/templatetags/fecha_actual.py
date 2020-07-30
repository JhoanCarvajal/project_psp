from django.template import Library
from datetime import datetime

register = Library()

@register.simple_tag()
def fecha_sistema():
    fecha = datetime.now()
    return fecha