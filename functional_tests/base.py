import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from bank.models import Card
from config.models.student import Student
from deploy.docker.app.init_db import main as init_db


MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        init_db()
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)

        self.mark = Student.objects.create(first_name='Mark',
                                               middle_name='Smithy',
                                               last_name='Smith',
                                               birth_day='1996-04-05',
                                               phone=12345678,
                                               grade=9,
                                               school='asdavfs',
                                               residency_area='Prague')
        self.daniel = Student.objects.create(first_name='Daniel',
                                               middle_name='Smithy',
                                               last_name='Smith',
                                               birth_day='1996-04-05',
                                               phone=12345678,
                                               grade=9,
                                               school='asdavfs',
                                               residency_area='Prague')
        self.sara = Student.objects.create(first_name='Sara',
                                               middle_name='Smithy',
                                               last_name='Smith',
                                               birth_day='1996-04-05',
                                               phone=12345678,
                                               grade=9,
                                               school='asdavfs',
                                               residency_area='Prague')

        self.card_mark = Card.objects.create(number=12345, holder=self.mark)
        self.card_daniel = Card.objects.create(number=54321, holder=self.daniel)
        self.card_sara = Card.objects.create(number=9999, holder=self.sara)

    def tearDown(self):
        self.browser.quit()

    @staticmethod
    def wait_for(fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
