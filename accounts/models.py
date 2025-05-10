from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('gerente', 'Gerente'),
        ('atendente', 'Atendente'),
        ('psicologo', 'Psicólogo'),
        ('paciente', 'Paciente'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='paciente')

    def is_paciente(self):
        return self.role == 'paciente'
