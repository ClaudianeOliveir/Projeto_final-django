from contextlib import _RedirectStream
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import Tarefa_Form ##Formulário sendo invocado aqui
##from django.utils import timezone
from Sistema.models import Usuario, Tarefa, Categoria


# Create your views here.
def Lista_Tarefas(request):
    print('Lista de Tarefas')
    template = loader.get_template("Sistema/base.html")  # Corrigi a chamada da função get_template
    return HttpResponse(template.render())

def Listas_Criadas(request):
    Tarefas = Tarefa.objects.all()
    print('Listas Criadas')
    return render (request, 'listas_criadas.html', {'Tarefas:Tarefas'})

def Criar_Tarefas(request):
    if request.method =='Post':
        form = Tarefa_Form(request.Post)
        if form.is_valid():
            print(request.POST.get('Tarefa'))##Debuging aqui
            nova_tarefa = form.save(commit=False)
            nova_tarefa.Usuario = request.POST.get('Usuario')
            nova_tarefa.Tarefa = request.POST.get('Tarefa') 
            nova_tarefa.save()
            return redirect('pagina_sucesso.html')
        else:
            form = Tarefa_Form()
    return render(request,'Sistema/Criar_Tarefas',{'form':form})
    ##return HttpResponse('Criar Tarefas')

##def Criar_Tarefas(request):
    if request.method == 'POST':
        form = Tarefa.Form(request.POST)
        try:
            if form.is_valid():
                nova_tarefa = form.save_and_commit(commit=False)
                nova_tarefa.Usuario = request.user
                return redirect('pagina_sucesso.html')
        except Exception as e:
            print(e)
            form = Tarefa.Form()

    return HttpResponse('Criar Tarefas')
