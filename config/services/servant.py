from config.models.servant import Servant


class ServantService:

    @staticmethod
    def create_servant(first_name, middle_name, last_name, birth_day, phone):
        Servant.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                               birth_day=birth_day, phone=phone)
