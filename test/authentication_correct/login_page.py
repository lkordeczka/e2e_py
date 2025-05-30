from selenium.webdriver.chrome.webdriver import WebDriver

from test.base_page import BasePage
from test.utils.locators import LoginPageLocators, DashboardPageLocators


class LoginPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def set_login(self, login: str) -> None:
        self.set_text(LoginPageLocators.USERNAME_INPUT, login)

    def set_password(self, password: str) -> None:
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    def login_as(self, login: str, password: str) -> None:
        self.set_login(login)
        self.set_password(password)
        self.press_submit_btn()

    def press_submit_btn(self) -> None:
        self.click(LoginPageLocators.SUBMIT_BTN)

    def submit_btn_exist(self) -> bool:
        return self.element_exists(LoginPageLocators.SUBMIT_BTN)

    def no_login_warning_text(self) -> str | None:
        return self.get_element_text(LoginPageLocators.NO_USERNAME_LABEL)

    def no_password_warning_text(self) -> str | None:
        return self.get_element_text(LoginPageLocators.NO_PASSWORD_LABEL)

    def dashboard_header_exist(self) -> bool:
        return self.element_exists(DashboardPageLocators.DASHBOARD_HEADER)
