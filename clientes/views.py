from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from viagens.models import Viagem
from django.db.models import Q

# Cadastro do cliente - formulário para criar clientes
def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cadastro_clientes.html', {'form': form})

# Listagem de clientes com busca pelo nome (case-insensitive)
def lista_clientes(request):
    busca = request.GET.get('busca', '')
    clientes = Cliente.objects.filter(nome__icontains=busca) if busca else Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes, 'busca': busca})

# Visualizar viagens de um cliente específico
def cliente_viagens(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    viagens = cliente.viagem_set.all()
    return render(request, 'clientes/cliente_viagens.html', {'cliente': cliente, 'viagens': viagens})
