from django.shortcuts import render, redirect
from .forms import ConsultaForm
from django.contrib.auth.decorators import login_required
from .models import Paciente


def home(request):
    return render(request, 'home.html')

@login_required
def agendar_consulta(request):
    paciente = Paciente.objects.get(user=request.user)

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