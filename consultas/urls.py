from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agendar/', views.agendar_consulta, name='agendar'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),    
]
