from config.services.bonus import BonusService
from config.services.user import UserService


def main():
    BonusService().add_bonus_values_if_not_exists(week=10, month=25, quarter=50)
    UserService().create_admin_if_doesnt_exist()
    UserService().create_guest_if_doesnt_exist()


if __name__ == 'django.core.management.commands.shell':
    main()
