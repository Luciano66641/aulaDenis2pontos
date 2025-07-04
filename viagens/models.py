from django.db import models

class Viagem(models.Model):
    destino = models.CharField(max_length=100)
    data_partida = models.DateField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    clientes = models.ManyToManyField('clientes.Cliente')

    def __str__(self):
        return self.destino.title()  # Regra 8 - capitalização
