from config.models.bonus import Bonus


class BonusService:

    def add_bonus_values(self, week, month, quarter):
        if self.record_exists():
            bonus = Bonus.objects.all()
            return bonus.update(WEEK=week, MONTH=month, QUARTER=quarter)
        return Bonus.objects.create(WEEK=week, MONTH=month, QUARTER=quarter)

    @staticmethod
    def record_exists() -> bool:
        return Bonus.objects.count()

    def add_bonus_values_if_not_exists(self, week, month, quarter):
        if not self.record_exists():
            return Bonus.objects.create(WEEK=week, MONTH=month, QUARTER=quarter)
