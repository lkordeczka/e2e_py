import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from test.authentication.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        driver_options.add_experimental_option(
            "prefs", {"profile.password_manager_leak_detection": False}
        )
        self.driver: WebDriver = webdriver.Chrome(options=driver_options)
        self.page = LoginPage(self.driver)
        self.driver.get("https://www.saucedemo.com/")

    def test_correct_login(self):
        """[LOGOWANIE 1] Poprawne logowanie. Użytkownik powinien zostać zalogowany do serwisu"""
        self.page.login_as("standard_user", "secret_sauce")

        self.assertIn("/inventory", self.page.get_actual_url())
        self.assertTrue(self.page.dashboard_is_visible(2))
        self.assertFalse(self.page.login_form_is_visible())

    def test_no_login(self):
        """[LOGOWANIE 2] Brak loginu. Proces logowania powinien zakończyć się błędem. Komunikat:
        'Username is required'."""

        # TODO W testach, które sprawdzają błędne logowania należy sprawdzić asercją czy:
        #  Czy system nie przekierował nas na adres /inventory
        #  Elementy dashboardu użytkownika są niewidoczne
        #  Elementy formularza logowania są widoczne
        #  Czy pojawił się odpowiedni komunikat
        pass

    def test_no_password(self):
        """[LOGOWANIE 3] Brak hasła. Proces logowania powinien zakończyć się błędem. Komunikat:
        'Password is required'."""
        # TODO
        pass

    def test_incorrect_login(self):
        """[LOGOWANIE 4] Błędny login. Proces logowania powinien zakończyć się błędem. Komunikat: 'Username or password
         do not match any user in this service'."""
        # TODO
        pass

    def test_incorrect_password(self):
        """[LOGOWANIE 5] Błędne hasło. Proces logowania powinien zakończyć się błędem. Komunikat: 'Username or password
         do not match any user in this service'. """
        # TODO
        pass

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
