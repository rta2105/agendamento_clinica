from django.db import models
from django.conf import settings

class Psicologo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    crp = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    especialidade = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.crp})"

class Paciente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

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
