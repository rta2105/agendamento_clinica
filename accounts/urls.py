from django.urls import path
from .views import (
    LoginGerenteView, LoginAtendenteView,
    dashboard_gerente, dashboard_atendente,
    cadastrar_usuario, cadastrar_paciente
)

urlpatterns = [
    path('login/gerente/', LoginGerenteView.as_view(), name='login_gerente'),
    path('login/atendente/', LoginAtendenteView.as_view(), name='login_atendente'),
    path('dashboard/gerente/', dashboard_gerente, name='dashboard_gerente'),
    path('dashboard/atendente/', dashboard_atendente, name='dashboard_atendente'),
    path('cadastrar/usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastrar/paciente/', cadastrar_paciente, name='cadastrar_paciente'),
]
