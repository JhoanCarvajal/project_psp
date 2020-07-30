from django.contrib import admin
from .models import RegistroTiempo

# Register your models here.
class RegistroTiempoAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio', 'comentarios')

admin.site.register(RegistroTiempo, RegistroTiempoAdmin)