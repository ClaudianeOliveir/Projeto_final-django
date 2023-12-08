from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 


# Create your views here.
def  Lista_Tarefas(request):
    print('Lista de Tarefas').get_template("sistema/base.html")
    template = loader
    return HttpResponse(template.render()) 

def Listas_Criadas(request):
    Print('Listas Criadas')
    return HttpResponse(Listas_Criadas)

def Criar_Tarefas(request):
    print('Criar Tarefas')
    return HttpResponse(Criar_Tarefas)