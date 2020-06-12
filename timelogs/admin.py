from django.contrib import admin
from .models import TimeLog

# Register your models here.

class TimeLogAdmin(admin.ModelAdmin):
    list_display = ('startDate', 'stopDate', 'updated')

admin.site.register(TimeLog, TimeLogAdmin)