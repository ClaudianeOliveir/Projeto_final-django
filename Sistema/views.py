from contextlib import _RedirectStream
from django.template import TemplateDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date
#from .forms import Tarefa_Form ##Formulário sendo invocado aqui
##from django.utils import timezone
from Sistema.models import Usuario,Tarefa


# Create your views here.
def Home(redirect):## Página inicial do projeto
    print('HOME')
    try:
        return render(redirect, "base.html")
    except TemplateDoesNotExist:
        return HttpResponse("Template não encontrado.")
    ##return HttpResponse(template.render())

def Listas_Criadas(request): ##Mostra as tarefas presentes no banco de dados
    Tarefas = Tarefa.objects.all()
    print('REQUISIÇÃO PARA LISTAS CRIADAS ACEITA')
    return render(request, 'listas_criadas.html', {'Tarefas': Tarefas})


def Criar_Tarefas(redirect): ##Ao acessar o link, joga para o formulário
    print("FORMULÁRIO INICIADO")
    template = loader.get_template("forms.html")
    return HttpResponse(template.render())

def Forms(request): ##Recebe valores POST do formulario e processa. Caso dê certo, salva no banco.
    print("PROCESSO DE REQUISIÇÃO INICIADO")
    form = Tarefa.objects.all()
    ##user = Usuario.objects.nome()

    if request.method == 'POST':
        print("REQUISIÇÃO ACEITA")
        data_padrao_tupla = (2024, 10, 20)
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        proprietario = request.POST.get('proprietario')
        data_finalizacao = date(*data_padrao_tupla)
        concluida = 1
        try:
            proprietario = Usuario.objects.get(nome=proprietario)
        except Usuario.DoesNotExist:
            print("USUÁRIO NÃO EXISTE")
            return HttpResponse("Usuário não encontrado.")
        print(f"Titulo: {titulo}, Descrição: {descricao}, Proprietário: {proprietario}")
        nova_tarefa = Tarefa(
            titulo=titulo,
            descricao=descricao,
            proprietario=proprietario,
            data_finalizacao=data_finalizacao,
            concluida=concluida
        )
        nova_tarefa.save()
        print("OPERAÇÃO CONCLUÍDA")
        return render(request, 'pagina_sucesso.html', {'titulo': titulo, 'descricao': descricao, 'proprietario': proprietario})
    else:
        print("ERRO AO REQUISITAR FORMULÁRIO")
        form = Tarefa.objects.all()

    return render(request, 'forms.html', {'form': form})

    


def Criar_Tarefas000(request): ## <---- Simulacro de view, ignorar!
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
