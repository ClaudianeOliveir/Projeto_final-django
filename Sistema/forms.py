from django import forms 
from Sistema.models import Tarefa 

class TarefaForm(forms.ModelForm):
    class meta: 
        model = Tarefa 
        filds = ['titulo', 'descricao'] 

        widgets = {
            'descricao': forms.Textarea(attrs={'rows':4, 'cols': 40}),
        }