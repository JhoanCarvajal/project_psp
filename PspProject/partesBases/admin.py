from django.contrib import admin
from .models import PartesBase

# Register your models here.
class PartesBaseAdmin(admin.ModelAdmin):
    list_display = ('baseplan', 'actualBase')

admin.site.register(PartesBase, PartesBaseAdmin)