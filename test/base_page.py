from typing import Tuple, Any

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self._driver: WebDriver = driver
        self.__wait: WebDriverWait = WebDriverWait(self._driver, 4)

    def click(self, locator: Tuple[Any, str]) -> None:
        self.__wait.until(EC.element_to_be_clickable(locator)).click()

    def set_text(self, locator: Tuple[Any, str], text: str) -> None:
        self.__wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def find(self, locator) -> WebElement:
        return self._driver.find_element(*locator)

    def get_actual_url(self) -> str:
        return self._driver.current_url

    def element_exists(self, locator: Tuple[Any, str]) -> bool:
        if self.get_element_if_exist(locator):
            return True
        return False

    def get_element_if_exist(self, locator: Tuple[Any, str]) -> WebElement | None:
        try:
            return self.__wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None

    def get_element_text(self, locator: Tuple[Any, str]) -> str | None:
        element: WebElement = self.get_element_if_exist(locator)
        if element:
            return element.text
        return None
