from config.models.discount import Discount


class DiscountSelector:

    @staticmethod
    def get_basic_discount():
        return Discount.objects.get().BASIC

    @staticmethod
    def get_gold_discount():
        return Discount.objects.get().GOLD

    @staticmethod
    def get_plat_discount():
        return Discount.objects.get().PLATINUM

    @staticmethod
    def get_discount_values():
        return Discount.objects.get()
