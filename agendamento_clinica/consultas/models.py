from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models.py
class Psicologo(models.Model):
    nome = models.CharField(max_length=100)
    crp = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    especialidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.crp})"

class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)

    class Meta:
        unique_together = ('psicologo', 'data', 'horario')

    def __str__(self):
        return f"{self.paciente} com {self.psicologo} em {self.data} às {self.horario}"
