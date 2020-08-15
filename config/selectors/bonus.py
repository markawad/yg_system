from config.models.bonus import Bonus


class BonusSelector:

    @staticmethod
    def get_weekly_bonus():
        return Bonus.objects.get().WEEK

    @staticmethod
    def get_monthly_bonus():
        return Bonus.objects.get().MONTH

    @staticmethod
    def get_quarterly_bonus():
        return Bonus.objects.get().QUARTER

    @staticmethod
    def get_bonus_values():
        return Bonus.objects.get()
