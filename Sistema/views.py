from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def  Lista_Tarefas(request):
    print('Lista de Tarefas')
    return HttpResponse('Lista_Tarefas')  

def Criar_Tarefas(request):
    print('Criar Tarefas')
    return HttpResponse(Criar_Tarefas)