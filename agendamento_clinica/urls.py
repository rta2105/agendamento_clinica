from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from accounts.views import (
    dashboard_gerente,
    dashboard_atendente,
    cadastrar_usuario,
    cadastrar_paciente,
)
from consultas import views as consultas_views
from accounts.forms import CustomLoginForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView


# View personalizada para login com redirecionamento baseado no papel
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        user = self.request.user
        if user.role == 'gerente':
            return redirect('dashboard_gerente')
        elif user.role == 'atendente':
            return redirect('dashboard_atendente')
        else:
            return redirect('agendar')


urlpatterns = [
    path('admin/', admin.site.urls),

    # Páginas principais
    path('', consultas_views.home, name='home'),
    path('agendar/', consultas_views.agendar_consulta, name='agendar'),
    path('confirmacao/', consultas_views.confirmacao, name='confirmacao'),

    # Autenticação
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # Dashboards
    path('dashboard/gerente/', dashboard_gerente, name='dashboard_gerente'),
    path('dashboard/atendente/', dashboard_atendente, name='dashboard_atendente'),

    # Gerente e Atendente
    path('accounts/cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('accounts/cadastrar_paciente/', cadastrar_paciente, name='cadastrar_paciente'),

    # Recuperação e alteração de senha
    path('accounts/password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
