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
    template = loader.get_template("base.html")  # Corrigi a chamada da função get_template
    return HttpResponse(template.render())

def Listas_Criadas(request):
    Tarefas = Tarefa.objects.all()
    print('Listas Criadas')
    return render(request, 'listas_criadas.html', {'Tarefas': Tarefas})


def Criar_Tarefas(request): ## "Se funciona, deixe queto."
    form2 = Tarefa.objects.all()
    
    if request.method == 'POST':
        form = Tarefa_Form(request.POST)
        
        if form.is_valid():
            nova_tarefa = form.save(commit=False)
            nova_tarefa.Usuario = form.cleaned_data.get('Usuario')
            nova_tarefa.Tarefa = form.cleaned_data.get('Tarefa')
            nova_tarefa.save()
            return redirect('Sistema:pagina_sucesso')
    else:
        form = Tarefa_Form()

    return render(request, 'pagina_sucesso.html', {'form2': form2, 'form': form})
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
