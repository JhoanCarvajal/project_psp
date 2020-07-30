from django.contrib import admin
from .models import Reporte

# Register your models here.
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'objetivos', 'numero_test')

admin.site.register(Reporte, ReporteAdmin)