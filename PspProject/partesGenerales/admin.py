from django.contrib import admin
from .models import PartesGeneral

# Register your models here.
class PartesGeneralAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tamaño_actual')

admin.site.register(PartesGeneral, PartesGeneralAdmin)