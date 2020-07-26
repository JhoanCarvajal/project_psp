from django.contrib import admin
from .models import Programa

# Register your models here.
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')

admin.site.register(Programa, ProgramaAdmin)