from selenium.webdriver.chrome.webdriver import WebDriver

from test.base_page import BasePage
from test.utils.locators import CardManagement


class CartManagementPage(BasePage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)