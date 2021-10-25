from config.services.bonus import BonusService
from config.services.user import UserService

BonusService().add_bonus_values_if_not_exists(week=10, month=25, quarter=50)
UserService().create_guest_if_doesnt_exist()
