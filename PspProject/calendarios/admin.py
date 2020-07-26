from django.contrib import admin
from .models import Calendario

# Register your models here.
class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('fecha_semana', 'horas_acomuladas_actual', 'valor_actual')

admin.site.register(Calendario, CalendarioAdmin)