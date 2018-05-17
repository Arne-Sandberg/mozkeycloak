import os
from django.conf import settings
from django.core.management import call_command
from django.contrib.auth import get_user_model

def run():
    db_path = settings.DATABASES['default']['NAME']
    if os.path.isfile(db_path):
        os.unlink(db_path)
    call_command("migrate")
    User = get_user_model()
    User.objects.create_superuser(email="admin@admin", username="admin", password="admin")
    User.objects.create_user(email="admin@admins", username="biasa", password="biasa")
    
    