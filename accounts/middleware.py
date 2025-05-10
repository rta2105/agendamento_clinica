from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class PasswordChangeMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica se o usuário está autenticado e precisa trocar a senha
        if request.user.is_authenticated and getattr(request.user, 'must_change_password', False):
            # Define as URLs que o usuário ainda pode acessar
            allowed_paths = [
                reverse('password_change'),
                reverse('password_change_done'),
                reverse('logout'),
            ]

            # Permite acesso às rotas essenciais mesmo com flag ativa
            if request.path not in allowed_paths and not request.path.startswith('/static/') and not request.path.startswith('/admin/'):
                return redirect('password_change')
