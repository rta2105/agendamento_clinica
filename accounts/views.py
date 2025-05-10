from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from .forms import UsuarioForm, PacienteForm
from .models import CustomUser
from consultas.models import Paciente

def is_gerente(user):
    return user.is_authenticated and user.role == 'gerente'

@user_passes_test(is_gerente)
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Envio de e-mail com login e senha
            user.email_user(
                subject="Acesso à Clínica Estácio",
                message=f"Olá {user.username},\n\nSeu acesso foi criado com sucesso.\nLogin: {user.username}\nSenha: {form.cleaned_data['password']}\n\nAltere sua senha no primeiro acesso.",
                from_email="naoresponda@clinicaestacio.com"
            )

            return redirect('dashboard_gerente')
    else:
        form = UsuarioForm()
    return render(request, 'accounts/cadastro_usuario.html', {'form': form})

@user_passes_test(lambda u: u.is_authenticated and u.role in ['gerente', 'atendente'])
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_atendente' if request.user.role == 'atendente' else 'dashboard_gerente')
    else:
        form = PacienteForm()
    return render(request, 'accounts/cadastro_paciente.html', {'form': form})

def custom_login(request):
    return LoginView.as_view(template_name='accounts/login.html')(request)

@login_required
def dashboard_gerente(request):
    return render(request, 'accounts/dashboard_gerente.html')

@login_required
def dashboard_atendente(request):
    return render(request, 'accounts/dashboard_atendente.html')