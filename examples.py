import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Utwórz instancję obiektu Chromedriver

# CZ1 Podstawowa interakcja z elementami
# Przejdź do strony https://www.saucedemo.com/


# Wpisz login: standard_user

# Wpisz hasło: secret_sauce

# Kliknij w przycisk button

# Dodaj do koszyka koszulkę "Sauce Labs Bolt T-Shirt"
# xPath: "//div[@class='inventory_item'][.//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]"

# Sprawdź czy pojawiła się informacja o dodanym elemencie do koszyka, Wypisz ile produktów obecnie znajduje się w koszyku
# Element

# Sprawdź czy przycisku "Add to card" zamienił się na przycisk "Remove"

# CZ2 Nawigacja

# Przejdź do koszyka
