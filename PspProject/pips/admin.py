from django.contrib import admin
from .models import Pip

# Register your models here.
class PipAdmin(admin.ModelAdmin):
    list_display = ('fecha','descripcion','solucion')

admin.site.register(Pip, PipAdmin)