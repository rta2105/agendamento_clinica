from django.contrib import admin
from .models import Psicologo, Paciente, Consulta

@admin.register(Psicologo)
class PsicologoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crp', 'email', 'especialidade')
    search_fields = ('nome', 'crp')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'email')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'psicologo', 'data', 'horario')
    list_filter = ('data', 'psicologo')
    search_fields = ('paciente__nome', 'psicologo__nome')
