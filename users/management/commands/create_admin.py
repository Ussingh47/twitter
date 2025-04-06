from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Creates a superuser with predefined credentials'

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@example.com'
        password = '123'

        try:
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully!'))
        except IntegrityError:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" updated successfully!'))
