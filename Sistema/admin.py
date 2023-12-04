# No arquivo admin.py dentro do aplicativo "Sistema"
from django.contrib import admin
from django.apps import apps
from .models import Usuario, Categorias, Tarefas

admin.site.register(Usuario)
admin.site.register(Categorias)
admin.site.register(Tarefas)