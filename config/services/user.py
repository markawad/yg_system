import os
from django.contrib.auth.models import User


class UserService:

    @staticmethod
    def create_guest_if_doesnt_exist() -> User:
        return User.objects.get_or_create(username='guest', password='iamnotanadmin')[0]

    @staticmethod
    def get_guest() -> User:
        return User.objects.get(username='guest')

    @staticmethod
    def create_admin_if_doesnt_exist() -> User:
        return User.objects.get_or_create(username=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'),
                                          password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'),
                                          is_superuser=True,
                                          is_staff=True)
