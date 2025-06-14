import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from test.authentication.login_page import LoginPage
from test.cart_management.cart_management_page import CartManagementPage


class CartManagementTest(unittest.TestCase):

    def setUp(self):
        driver_options = Options()
        driver_options.add_experimental_option(
            "prefs", {"profile.password_manager_leak_detection": False}
        )
        self.driver: WebDriver = webdriver.Chrome(options=driver_options)
        self.page = CartManagementPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://www.saucedemo.com/")
        self.login_page.login_as("standard_user", "secret_sauce")

    def test_add_item(self):
        """[ZARZĄDZANIE KOSZYKIEM 1] Do koszyka powinny zostać dodane trzy produkty"""
        self.page.add_item_by_name("Sauce Labs Bike Light")
        self.page.add_item_by_name("Sauce Labs Bolt T-Shirt")
        self.page.add_item_by_name("Test.allTheThings() T-Shirt (Red)")

        self.assertEqual("3", self.page.get_shopping_cart_number())

        # TODO - W teście należy dodatkowo sprawdzić czy w koszyku znajdują się wszystkie trzy dodane produkty.
        #  W tym celu trzeba przejść do kszyka, pobrać listę produktów a następnie sprawdzić, czy:
        #  1. Liczba produktów się zgadza
        #  2. Czy dodane zostały właściwe produkty(Wystarczy sprawdzić po nazwach produktów)

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
