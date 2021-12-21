from typing import Optional

from attendance.models.day import Day
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist


class DaySelector:
    
    @staticmethod
    def get_dates_by_month(month, for_sunday_school=False, for_bible_study=False):
        return Day.objects.filter(date__month=month,
                                  date__year=timezone.localdate().today(),
                                  for_sunday_school=for_sunday_school,
                                  for_bible_study=for_bible_study)

    @staticmethod
    def get_date(for_sunday_school=False, for_bible_study=False):
        return Day.objects.get(date=timezone.localdate().today(),
                               for_sunday_school=for_sunday_school,
                               for_bible_study=for_bible_study)

    @staticmethod
    def get_date_of_last_time(for_sunday_school=False, for_bible_study=False):
        try:
            return Day.objects.filter(date__lt=timezone.localdate().today(),
                                      for_sunday_school=for_sunday_school,
                                      for_bible_study=for_bible_study).order_by('-date').first()
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_yesterday_or_none() -> Optional[Day]:
        yesterday = timezone.localdate().today() - timedelta(1)
        try:
            return Day.objects.filter(date=yesterday).first()
        except ObjectDoesNotExist:
            return None
