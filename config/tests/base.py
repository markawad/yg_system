from django.test import TestCase
from config import models


class BaseTestCase(TestCase):

    def setUp(self):
        self.servant = models.Servant.objects.create(first_name='John',
                                                     middle_name='Smithy',
                                                     last_name='Smith',
                                                     birth_day='1996-04-05',
                                                     phone=12345678)
        self.student = models.Student.objects.create(first_name='Mark',
                                                     middle_name='Smithy',
                                                     last_name='Smith',
                                                     birth_day='1996-04-05',
                                                     phone=12345678,
                                                     grade=9,
                                                     school='asdavfs',
                                                     mothers_number=113123,
                                                     fathers_number=123123,
                                                     father_of_confession='Father',
                                                     servant=self.servant,
                                                     residency_area='Prague')
        self.student2 = models.Student.objects.create(first_name='Mark2',
                                                      middle_name='Smithy2',
                                                      last_name='Smith2',
                                                      birth_day='1996-04-05',
                                                      phone=12345678,
                                                      grade=9,
                                                      school='asdavfs',
                                                      mothers_number=113123,
                                                      fathers_number=123123,
                                                      father_of_confession='Father',
                                                      servant=self.servant,
                                                      residency_area='Prague')
        self.alumni = models.Alumni.objects.create(first_name='Dani',
                                                   middle_name='Smithy',
                                                   last_name='Smith',
                                                   birth_day='1996-04-05',
                                                   phone=12345678,
                                                   graduation_year=2013)
