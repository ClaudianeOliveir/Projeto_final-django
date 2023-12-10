from contextlib import _RedirectStream
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from sistema.models import Usuario, Tarefa, Categoria


# Create your views here.
def Lista_Tarefas(request):
    print('Lista de Tarefas')
    template = loader.get_template("sistema/base.html")  # Corrigi a chamada da função get_template
    return HttpResponse(template.render())

def Listas_Criadas(request):
    Tarefas = Tarefa.objects.all()
    print('Listas Criadas')
    return render (request, 'listas_criadas.html', {'Tarefas:Tarefas'})

def Criar_Tarefas(request):
    if request.method =='Post':
        form = Tarefa.form(request.Post)
        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            nova_tarefa.Usuario = request.user 
            nova_tarefa.save()
            return redirect('pagina_sucesso.html')
        else:
            form = Tarefa.form()

    return HttpResponse('Criar Tarefas')