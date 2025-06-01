import unittest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from test.cart_management.cart_management_page import CartManagementPage


class CartManagementTest(unittest.TestCase):

    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome()
        self.page = CartManagementPage(self.driver)
        self.driver.get()

    def test_add_item(self):
        pass

    def remove_item(self):
        pass

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
