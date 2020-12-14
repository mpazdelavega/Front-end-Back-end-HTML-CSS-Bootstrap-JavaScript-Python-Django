from django.contrib import admin
from .models import Project

# Register your models here.

class ProyectAdmin(admin.ModelAdmin):
    readonly_fields =  ('created','update')

admin.site.register(Project,ProyectAdmin)
