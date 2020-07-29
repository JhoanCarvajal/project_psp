from django.contrib import admin
from .models import TiposDefecto

# Register your models here.
class TiposDefectoAdmin(admin.ModelAdmin):
    list_display= ('nombre',)
admin.site.register(TiposDefecto,TiposDefectoAdmin)