from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def Lista_Tarefas(request):
    template = loader.get_template("sistema/base.html")  # Corrigi a chamada da função get_template
    return HttpResponse(template.render())

def Listas_Criadas(request):
    print('Listas Criadas')
    return HttpResponse('Listas Criadas')

def Criar_Tarefas(request):
    print('Criar Tarefas')
    return HttpResponse('Criar Tarefas')