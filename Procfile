release: python manage.py makemigrations && python manage.py migrate
web: gunicorn snaptapapp_drf_api.wsgi