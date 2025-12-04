from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Проверка работы вкладок конструктора
class TestConstructorTabs:

    def open_constructor(self, driver, wait):
        driver.get(Data.STELLAR_URL)
        wait.until(EC.element_to_be_clickable(L.CONSTRUCTOR_BTN)).click()

    def click_tab(self, driver, wait, element, expected_text):
        tab = wait.until(EC.presence_of_element_located(element))
        driver.execute_script("arguments[0].click();", tab)
        wait.until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, expected_text))
        assert wait.until(EC.visibility_of_element_located(L.ACTIVE_TAB)).text == expected_text

    def test_go_to_buns_section(self, driver):
        wait = WebDriverWait(driver, 10)
        self.open_constructor(driver, wait)
        self.click_tab(driver, wait, L.BUNS_TAB, "Булки")

    def test_go_to_sauces_section(self, driver):
        wait = WebDriverWait(driver, 10)
        self.open_constructor(driver, wait)
        self.click_tab(driver, wait, L.SAUCES_TAB, "Соусы")

    def test_go_to_fillings_section(self, driver):
        wait = WebDriverWait(driver, 10)
        self.open_constructor(driver, wait)
        self.click_tab(driver, wait, L.FILLINGS_TAB, "Начинки")

