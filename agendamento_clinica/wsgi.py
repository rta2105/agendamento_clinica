import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agendamento_clinica.settings')

application = get_wsgi_application()
