from django.contrib import admin
from django.urls import path
from Sistema import views

app_name = 'Sistema'

urlpatterns = [
    # Mapeamento das páginas
    ##path('',views.Lista_Tarefas, name='Lista_Tarefas'),
    path('', views.Home, name='Home'),
    path('Forms/',views.Forms,name='Forms'),
    path('listas_criadas/', views.Listas_Criadas, name='Listas_Criadas'),  # Corrigi o nome da função
    path('Criar_Tarefas/', views.Criar_Tarefas, name='Criar_Tarefas'),
    path('pagina_sucesso/',views.Criar_Tarefas, name='pagina_sucesso')
]
