from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)##Optei por tipo emailfield mesmo, então usem no padrão de um email real(exemplo@teste.com.br)
    class Meta:
        verbose_name_plural = "Usuarios"
class Tarefas(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    data_finalizacao = models.DateField()
    concluida = models.BooleanField()

    def __str__(self):
        return f'{self.descricao}'
    
    def Propreitario(self):
        ##Alterar aqui!!!!! isso é uma chave estrangeira, resolver a relação depois com a class Usuario.
        pass

    class Meta:
        verbose_name_plural = "Tarefas"
class Categorias(models.Model):
    nome_cat = models.CharField(max_length=50)

    def Tarefas(self):
        ##Alterar isso aqui!##
        pass
    class Meta:
        verbose_name_plural = "Categorias"