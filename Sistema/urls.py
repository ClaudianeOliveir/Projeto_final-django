from django.contrib import admin
from django.urls import path
from Sistema import views

urlpatterns = [
    # Mapeamento das páginas
    path('Lista_Tarefas', views.Lista_Tarefas, name='Lista_Tarefas'),
    path('Listas_Criadas', views.Listas_Criadas, name='Listas_Criadas'),  # Corrigi o nome da função
    path('Criar_Tarefas', views.Criar_Tarefas, name='Criar_Tarefas'),
]