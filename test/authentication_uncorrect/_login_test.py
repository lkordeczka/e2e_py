import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.wait: WebDriverWait = WebDriverWait(self.driver, 4)

    def test_correct_login(self):
        """[LOGOWANIE.1] Użytkownik powinien zostać przekierowany na stronę 'dahboard'"""

        self.wait.until(EC.visibility_of_element_located((By.NAME, 'username'))).send_keys('Admin')
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('admin123')
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button.orangehrm-login-button'))).click()

        try:
            # Czekaj na załadowanie strony
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.oxd-topbar-header')))
        except:
            pass

        self.assertIn("/dashboard/", self.driver.current_url)

    def test_no_user_name(self):
        """[LOGOWANIE.2] Użytkownik powinien pozostać na stronie logowania. Powinien pojawić się komunikat
        o konieczności wpisania loginu w formularzu"""
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys('admin123')
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'button.orangehrm-login-button'))).click()

        self.assertIn("/auth/login", self.driver.current_url)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
