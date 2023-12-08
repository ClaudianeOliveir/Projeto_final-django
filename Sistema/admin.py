# No arquivo admin.py dentro do aplicativo "Sistema"
from django.contrib import admin
from django.apps import apps
from .models import Usuario, Categoria, Tarefa

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Tarefa)