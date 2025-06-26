from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'cpf', 'email']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
