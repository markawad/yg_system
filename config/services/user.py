import os
from django.contrib.auth.models import User


class UserService:

    @staticmethod
    def create_guest_if_doesnt_exist() -> User:
        user = User.objects.get_or_create(username='guest')[0]
        user.set_password('iamnotanadmin')
        return user.save()

    @staticmethod
    def get_guest() -> User:
        return User.objects.get(username='guest')

    @staticmethod
    def create_admin_if_doesnt_exist() -> User:
        if not User.objects.filter(username='admin').exists():
            user = User.objects.create(username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
                                       is_superuser=True,
                                       is_staff=True)
            user.set_password(os.environ.get('DJANGO_SUPERUSER_PASSWORD'))
            return user.save()
