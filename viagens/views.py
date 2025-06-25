from django.shortcuts import render, redirect, get_object_or_404
from .models import Viagem
from .forms import ViagemForm

# Template 3: nova_viagem.html
def nova_viagem(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_viagens')
    else:
        form = ViagemForm()
    return render(request, 'viagens/nova_viagem.html', {'form': form})

# Template 4: lista_viagens.html
def lista_viagens(request):
    viagens = Viagem.objects.all()
    return render(request, 'viagens/lista_viagens.html', {'viagens': viagens})

# Template 6: viagem_por_clientes.html
def viagem_por_clientes(request, viagem_id):
    viagem = get_object_or_404(Viagem, id=viagem_id)
    clientes = viagem.clientes.all()
    return render(request, 'viagens/viagem_por_clientes.html', {'viagem': viagem, 'clientes': clientes})
