from django.contrib import admin
from .models import PartesAñadida

# Register your models here.
class PartesAñadidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'items_planeados', 'items_acuales')

admin.site.register(PartesAñadida, PartesAñadidaAdmin)