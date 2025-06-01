import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfiguracja opcji Chrome
# "credentials_enable_service": False - wyłącza usługę zarządzania poświadczeniami Google.
# "profile.password_manager_enabled": False  - wyłącza menedżera haseł w profilu przeglądarki.
# "profile.password_manager_leak_detection": False - wyłącza komunikat o wycieku

# chrome_options.add_argument("--headless=new")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,  # wyłącza usługę zarządzania poświadczeniami Google.
    "profile.password_manager_enabled": False,  # wyłącza menedżera haseł w profilu przeglądarki.
    "profile.password_manager_leak_detection": False #  wyłącza komunikat o wycieku
})

# Utwórz instancję obiektu Chromedriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

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
# xPath: "//div[@class='inventory_item'][.//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]"
item_xpath = r"//div[@class='inventory_item'][.//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]"
item = driver.find_element(By.XPATH, item_xpath)
item.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

# Sprawdź czy pojawiła się informacja o dodanym elemencie do koszyka, Wypisz ile produktów obecnie znajduje się w koszyku
# Element
number_of_products = driver.find_element(By.ID, "shopping_cart_container").text
assert number_of_products == "1", "Nie zgadza się liczba produktów"

# Sprawdź czy przycisku "Add to card" zamienił się na przycisk "Remove"

# CZ2 Nawigacja

# Przejdź do koszyka
