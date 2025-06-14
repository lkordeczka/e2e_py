from typing import Tuple, Any

from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver: WebDriver = driver
        self.__wait: WebDriverWait = WebDriverWait(self._driver, 4)

    def click(self, locator: Tuple[Any, str]) -> None:
        self.__wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator) -> WebElement:
        return self._driver.find_element(*locator)

    def get_actual_url(self) -> str:
        return self._driver.current_url

    def element_exists(self, locator: Tuple[Any, str], wait: int = 0) -> bool:
        try:
            wait_for_element: WebDriverWait = WebDriverWait(self._driver, wait)
            wait_for_element.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False