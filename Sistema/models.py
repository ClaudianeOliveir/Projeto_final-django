from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)##Optei por tipo emailfield mesmo, então usem no padrão de um email real(exemplo@teste.com.br)

    def __str__(self):
        return f'{self.nome}'
    class Meta:
        verbose_name_plural = "Usuarios"



class Tarefa(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    data_finalizacao = models.DateField()
    concluida = models.BooleanField()
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return f'{self.descricao}'

    class Meta:
        verbose_name_plural = "Tarefas"


        
class Categoria(models.Model):
    op1 = 'Manutenção'; op2 = 'Movimentação'
    op3 = 'Compra/Venda'; op4 = 'Desconhecido/Desaparecido'; op5 = 'Stand-by'
    OPCOES_LISTA = [
        (op1, 'Manutenção'),
        (op2, 'Movimentação'),
        (op3, 'Compra/Venda'),
        (op4, 'Desconhecido/Desaparecido'),
        (op5, 'Stand-by')
    ]
    nome_categoria = models.CharField(max_length=50)
    Tarefas = models.ManyToManyField('Tarefa')
    Tipo = models.CharField(
        max_length=50,
        choices=OPCOES_LISTA,
        default=op5
    )

    def __str__(self):
        return f'{self.nome_categoria} --- {self.Tipo}'
    class Meta:
        verbose_name_plural = "Categorias"
