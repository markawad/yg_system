from config.models.alumni import Alumni


class AlumniSelector:

    @staticmethod
    def get_all_alumni_count():
        return Alumni.objects.count()
