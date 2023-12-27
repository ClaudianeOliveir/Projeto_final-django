from django.contrib import admin
from django.urls import path
from Sistema import views

urlpatterns = [
    # Mapeamento das páginas
    ##path('',views.Lista_Tarefas, name='Lista_Tarefas'),
    path('', views.Lista_Tarefas, name='Lista_Tarefas'),
    ##path('Formulario',views.Formulario,name='Formulario'), ---- Essa linha é uma ideia apenas, talvez exista em algum ponto ou não
    path('Listas_Criadas', views.Listas_Criadas, name='Listas_Criadas'),  # Corrigi o nome da função
    path('Criar_Tarefas', views.Criar_Tarefas, name='Criar_Tarefas')
]
