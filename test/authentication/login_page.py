from selenium.webdriver.chrome.webdriver import WebDriver

from test.base_page import BasePage
from test.utils.locators import Dashboard, Login


class LoginPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def login_as(self, login, password):
        self._driver.find_element(*Login.INPUT_LOGIN).send_keys(login)
        self._driver.find_element(*Login.INPUT_PASSWORD).send_keys(password)
        self._driver.find_element(*Login.LOGIN_BTN).click()

    def dashboard_is_visible(self, wait: int = 0):
        return self.element_exists(Dashboard.INVENTORY_LIST, wait) and self.element_exists(Dashboard.INVENTORY_LIST)

    def login_form_is_visible(self):
        return (
                self.element_exists(Login.LOGIN_BTN) and
                self.element_exists(Login.INPUT_LOGIN) and
                self.element_exists(Login.INPUT_PASSWORD)
        )
