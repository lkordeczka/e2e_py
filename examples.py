import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Utwórz instancję obiektu Chromedriver
driver_options = Options()
driver_options.add_experimental_option(
    "prefs", {"profile.password_manager_leak_detection": False}
)
driver = webdriver.Chrome(options=driver_options)

# CZ1 Podstawowa interakcja z elementami
# Przejdź do strony https://www.saucedemo.com/
driver.get("https://www.saucedemo.com/")

# Wpisz login: standard_user
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Wpisz hasło: secret_sauce
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Kliknij w przycisk button
driver.find_element(By.ID, "login-button").click()

# Dodaj do koszyka koszulkę "Sauce Labs Bolt T-Shirt"
# xPath = r"//div[@class='inventory_item'][.//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]"
# item = driver.find_element(By.XPATH, xPath)
# item.find_element(By.CSS_SELECTOR, "button").click()
items = driver.find_elements(By.CSS_SELECTOR, "div.inventory_item")
for item in items:
    item.find_element(By.CSS_SELECTOR, "button").click()



# Sprawdź czy pojawiła się informacja o dodanym elemencie do koszyka, Wypisz ile produktów obecnie znajduje się w koszyku
# Element

# Sprawdź czy przycisku "Add to card" zamienił się na przycisk "Remove"

# CZ2 Nawigacja

# Przejdź do koszyka


time.sleep(100000)