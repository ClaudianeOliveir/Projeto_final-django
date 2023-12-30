from django import forms 
from .models import Tarefa 

#class Tarefa_Form(forms.ModelForm):
    #class Meta: 
        #model = Tarefa 
        #fields = ['titulo', 'descricao']
        #exclude = ['data_finalizacao','concluida','proprietario'] 

        #widgets = {
        #    'descricao': forms.Textarea(attrs={'rows':4, 'cols': 40}),
        #}