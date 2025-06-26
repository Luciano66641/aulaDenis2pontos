from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome.title()
