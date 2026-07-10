import os
import django

settings_module = None
for root, dirs, files in os.walk('.'):
    if 'settings.py' in files and '__init__.py' in files:
        folder_name = os.path.basename(root)
        settings_module = f"{folder_name}.settings"
        break

if settings_module:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    django.setup()

    from django.contrib.auth.models import User
    username = os.environ.get('ADMIN_USERNAME')
    password = os.environ.get('ADMIN_PASSWORD')

    if username and password:
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email='admin@artdiju.com.br', password=password)
        else:
            u = User.objects.get(username=username)
            u.set_password(password)
            u.save()