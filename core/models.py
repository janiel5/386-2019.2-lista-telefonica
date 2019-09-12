from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    endereco =models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
