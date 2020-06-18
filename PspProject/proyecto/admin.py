from django.contrib import admin
from .models import Proyect
# Register your models here.

admin.site.register(Proyect)

title="PSP"
subtitle="Panel de gestión"

admin.site.site_header=title
admin.site.site_title=title
admin.site.index_title=subtitle