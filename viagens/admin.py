from django.contrib import admin
from .models import Viagem

@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('destino', 'data_partida', 'preco')
