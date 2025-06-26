from django import forms
from .models import Viagem

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['destino', 'data_partida', 'preco', 'clientes']
        widgets = {
            'data_partida': forms.DateInput(attrs={'type': 'date'}),
            'clientes': forms.CheckboxSelectMultiple(),
        }
