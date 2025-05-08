#!/usr/bin/env bash
# build.sh

# Instala dependências
pip install -r requirements.txt

# Executa migrações
python manage.py migrate

# Coleta arquivos estáticos
python manage.py collectstatic --noinput
