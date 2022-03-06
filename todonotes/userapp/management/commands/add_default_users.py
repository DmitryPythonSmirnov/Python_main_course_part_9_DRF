from userapp.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
        User.objects.create_user('django1', 'django1@gb.local', 'django1')
        User.objects.create_user('django2', 'django2@gb.local', 'django2')
        User.objects.create_user('django3', 'django3@gb.local', 'django3')
