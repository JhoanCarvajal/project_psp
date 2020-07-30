from django.contrib import admin
from .models import PartesReusada

# Register your models here.
class PartesReusadaAdmin(admin.ModelAdmin):
    list_display = ('plan', 'actual')

admin.site.register(PartesReusada, PartesReusadaAdmin)