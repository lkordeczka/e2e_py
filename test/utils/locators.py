from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_INPUT = (By.NAME, 'username')
    NO_USERNAME_LABEL = (By.CSS_SELECTOR, 'form > input + .oxd-form-row .oxd-text')
    PASSWORD_INPUT = (By.NAME, 'password')
    NO_PASSWORD_LABEL = (By.CSS_SELECTOR, 'form > input + .oxd-form-row + div .oxd-text')
    SUBMIT_BTN = (By.CSS_SELECTOR, 'button.orangehrm-login-button')
    ERROR_MESSAGE = (By.ID, 'error')


class DashboardPageLocators(object):
    DASHBOARD_HEADER = (By.CSS_SELECTOR, '.oxd-topbar-header')
