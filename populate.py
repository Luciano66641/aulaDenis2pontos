import os
import django
from datetime import date
from django.apps import apps

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoViagem.settings')
django.setup()

# Recupera os modelos dinamicamente
Cliente = apps.get_model('clientes', 'Cliente')
Viagem = apps.get_model('viagens', 'Viagem')

# Limpa os dados anteriores (opcional, use com cuidado)
Cliente.objects.all().delete()
Viagem.objects.all().delete()

# Membros do grupo (Regra 10)
clientes_data = [
    {"nome": "Ana Souza", "data_nascimento": "1995-03-10", "cpf": "111.111.111-11", "email": "ana@example.com"},
    {"nome": "Carlos Lima", "data_nascimento": "1994-07-15", "cpf": "222.222.222-22", "email": "carlos@example.com"},
    {"nome": "Mariana Dias", "data_nascimento": "1993-09-21", "cpf": "333.333.333-33", "email": "mariana@example.com"},
    {"nome": "Pedro Henrique", "data_nascimento": "1990-11-05", "cpf": "444.444.444-44", "email": "pedro@example.com"},
    {"nome": "João Vitor", "data_nascimento": "1998-01-12", "cpf": "555.555.555-55", "email": "joao@example.com"},
]

# Clientes adicionais
clientes_data += [
    {"nome": "Lucas Mendes", "data_nascimento": "1992-06-25", "cpf": "666.666.666-66", "email": "lucas@example.com"},
    {"nome": "Fernanda Silva", "data_nascimento": "1997-10-08", "cpf": "777.777.777-77", "email": "fernanda@example.com"},
    {"nome": "Julia Rocha", "data_nascimento": "1996-12-30", "cpf": "888.888.888-88", "email": "julia@example.com"},
    {"nome": "Ricardo Alves", "data_nascimento": "1991-05-14", "cpf": "999.999.999-99", "email": "ricardo@example.com"},
    {"nome": "Patricia Gomes", "data_nascimento": "1995-04-04", "cpf": "000.000.000-00", "email": "patricia@example.com"},
]

# Criação dos clientes
clientes_obj = []
for data in clientes_data:
    cliente = Cliente.objects.create(**data)
    clientes_obj.append(cliente)

# Criação de viagens com associação a alguns clientes
viagem1 = Viagem.objects.create(destino="Rio de Janeiro", data_partida=date(2025, 7, 10), preco=800.00)
viagem1.clientes.set(clientes_obj[:5])  # primeiros 5 clientes

viagem2 = Viagem.objects.create(destino="Salvador", data_partida=date(2025, 8, 5), preco=950.00)
viagem2.clientes.set(clientes_obj[5:])  # últimos 5 clientes

viagem3 = Viagem.objects.create(destino="São Paulo", data_partida=date(2025, 9, 15), preco=700.00)
viagem3.clientes.set(clientes_obj[::2])  # clientes alternados

print("✅ População finalizada com sucesso.")
