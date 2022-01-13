from functional_tests.base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import os
import time


class Attendance(FunctionalTest):

    def test_users_can_log_attendance_on_the_go(self):
        # Alice logs in to the website as admin
        self.browser.get(self.live_server_url)

        user_input: WebElement = self.wait_for(lambda: self.browser.find_element_by_id('id_username'))
        pass_input: WebElement = self.wait_for(lambda: self.browser.find_element_by_id('id_password'))

        user_input.send_keys('admin')
        pass_input.send_keys(os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin'))
        pass_input.send_keys(Keys.ENTER)

        # assert Alice is logged in as admin
        time.sleep(2)
        self.assertIn('Log Out', self.browser.page_source)

        # She opens the attendance for Sunday School service to start logging students
        self.wait_for(lambda: self.browser.find_element_by_link_text('Attendance')).click()
        self.wait_for(lambda: self.browser.find_element_by_id('id_sunday_school')).submit()

        # Mark comes in and places his ID on the RFID card reader and his attendance his counted
        card_input: WebElement = self.wait_for(lambda: self.browser.find_element_by_id('card_number'))
        card_input.send_keys(self.mark.card.number)
        card_input.send_keys(Keys.ENTER)

        # assert Mark's attendance is recorded
        time.sleep(2)
        self.assertIn('Attendance Count: 1', self.browser.page_source)

        # success



