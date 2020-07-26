from django.contrib import admin
from .models import Profesor

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('id_usuario','rol')

admin.site.register(Profesor, ProfesorAdmin)
