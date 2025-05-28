import unittest
import page
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")

driver.find_element(By.ID, "L2AGLb").click()
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultPage(self.driver)
        assert search_results_page.is_results_found(), "Nie znaleziono."

    def tearDown(self):
        self.driver.close()