import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from test.authentication_correct.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome()
        self.page = LoginPage(self.driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com")

    def test_correct_login(self):
        """[LOGOWANIE.1] Użytkownik powinien zostać przekierowany na stronę 'dahboard'"""
        self.page.login_as("Admin", "admin123")

        self.assertTrue(self.page.dashboard_header_exist())
        self.assertIn("/dashboard/", self.page.get_actual_url())
        self.assertFalse(self.page.submit_btn_exist())

    def test_no_user_name(self):
        """[LOGOWANIE.2] Użytkownik powinien pozostać na stronie logowania. Powinien pojawić się komunikat
        o konieczności wpisania loginu w formularzu"""
        self.page.set_password("admin123")
        self.page.press_submit_btn()

        self.assertIn("/auth/login", self.page.get_actual_url())
        self.assertEqual("Required", self.page.no_login_warning_text())
        self.assertIsNone(self.page.no_password_warning_text())
        self.assertTrue(self.page.submit_btn_exist())

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()
