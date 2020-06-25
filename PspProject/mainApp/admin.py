from django.contrib import admin
from .models import Lenguaje, Medida

# Register your models here.
class LenguajeAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Lenguaje,LenguajeAdmin)

class MedidaAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Medida,MedidaAdmin)