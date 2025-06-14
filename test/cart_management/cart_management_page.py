from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test.base_page import BasePage
from test.utils.locators import CardManagement, Login


class CartManagementPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_item_by_name(self, name):
        xpath = rf"//div[@class='inventory_item'][.//div[contains(text(), '{name}')]]"
        self._driver.find_element(By.XPATH, xpath).find_element(By.CSS_SELECTOR, "button").click()

    def get_shopping_cart_number(self):
        return self._driver.find_element(*CardManagement.SHOPPING_CART_CONTAINER).text
