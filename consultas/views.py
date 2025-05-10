from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsultaForm
from django.contrib.auth.decorators import login_required
from .models import Paciente
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

@login_required
def agendar_consulta(request):
    try:
        paciente = get_object_or_404(Paciente, user=request.user)
    except:
        messages.error(request, "Seu perfil de paciente não foi encontrado. Entre em contato com a secretaria.")
        return redirect('home')

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.save()
            return redirect('confirmacao')
    else:
        form = ConsultaForm()

    return render(request, 'agendar.html', {'form': form})

def confirmacao(request):
    return render(request, 'confirmacao.html')
