from django.contrib import admin

from notesapp.models import Project, ToDo

admin.site.register(Project)
admin.site.register(ToDo)
