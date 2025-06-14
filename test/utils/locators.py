from selenium.webdriver.common.by import By


class Login:
    INPUT_LOGIN = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")


class Dashboard:
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    MENU_BTN = (By.ID, "react-burger-menu-btn")


class CardManagement:
    SHOPPING_CART_CONTAINER = (By.ID, "shopping_cart_container")
