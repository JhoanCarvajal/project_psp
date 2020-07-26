from django.contrib import admin
from .models import Lenguaje, Medida, Proceso, Fase, TiposDefecto, TiposParte, TamañoItem

# Register your models here.
class LenguajeAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Lenguaje,LenguajeAdmin)

class MedidaAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Medida,MedidaAdmin)

class ProcesoAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Proceso,ProcesoAdmin)

class FaseAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(Fase,FaseAdmin)

class TiposDefectoAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(TiposDefecto,TiposDefectoAdmin)

class TiposParteAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(TiposParte,TiposParteAdmin)

class TamañoItemAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(TamañoItem,TamañoItemAdmin)