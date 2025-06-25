from django import forms
from .models import Viagem

class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['destino', 'data_partida', 'preco', 'clientes']
        widgets = {
            'clientes': forms.CheckboxSelectMultiple()
        }
