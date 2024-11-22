from django.contrib import admin
from .models import Temperatures

# Register your models here.
@admin.register(Temperatures)
class TemperaturesAdmin(admin.ModelAdmin):
    list_display = ('date', 'temperature1', 'humidity1', 
                    'temperature2', 'humidity2', 
                    'temperature3', 'humidity3', 
                    'temperature4', 'humidity4', 
                    'temperature5', 'humidity5', 
                    'time', )
    search_fields = ('date',)
    list_filter = ('date',)
