from config.models.discount import Discount


class DiscountService:

    def add_discount_values(self, basic, gold, platinum):
        if self.record_exists():
            discount = Discount.objects.all()
            return discount.update(BASIC=basic, GOLD=gold, PLATINUM=platinum)
        return Discount.objects.create(BASIC=basic, GOLD=gold, PLATINUM=platinum)
        
    @staticmethod
    def record_exists() -> bool:
        return Discount.objects.count()

    @staticmethod
    def save(obj):
        return obj.save()
