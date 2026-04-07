from django.contrib import admin
from .models import Reading 

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ['sensor_name', 'value', 'unit', 'recorded_at']
    list_filter = ['sensor_name', 'unit']
    