from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    # definir las como tupla simpre
    readonly_fields = ('created','updated')
# Register your models here.
admin.site.register(Project, ProjectAdmin)
