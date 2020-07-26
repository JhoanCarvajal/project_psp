from django.contrib import admin
from .models import RegistroDefecto

# Register your models here.
class RegistroDefectoAdmin(admin.ModelAdmin):
    list_display = ('fecha_encontrado', 'id_fase_creacion', 'tiempo_arreglo')

admin.site.register(RegistroDefecto, RegistroDefectoAdmin)