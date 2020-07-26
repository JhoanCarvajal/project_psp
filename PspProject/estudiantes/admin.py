from django.contrib import admin
from .models import Estudiante

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_usuario',)


admin.site.register(Estudiante, EstudianteAdmin)