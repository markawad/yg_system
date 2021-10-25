from django.contrib.auth.models import User


class UserService:

    @staticmethod
    def create_guest_if_doesnt_exist() -> User:
        return User.objects.get_or_create(username='guest', password='iamnotanadmin')[0]

    @staticmethod
    def get_guest() -> User:
        return User.objects.get(username='guest')
