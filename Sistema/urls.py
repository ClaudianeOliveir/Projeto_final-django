from django.contrib import admin 
from django.urls import nath 
from Sistema import views 

#importando views 

urlpatterns = [
    #mapeamento das paginas 
    path('Lista_Tarefas',views.Lista_Tarefas, name='Lista_Tarefas')
    path('Criar_Tarefas', views.Criar_Tarefas, name='Criar_Tarefas')
]