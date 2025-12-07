from selenium.webdriver.chrome.webdriver import WebDriver
from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Проверка работы вкладок конструктора
class TestConstructorTabs:

    def test_buns_cross(self, driver):
        driver.find_element(*L.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*L.SAUCES_TAB))
        driver.find_element(*L.BUNS_TAB)
        buns_span = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(*L.BUNS_TAB))

        assert buns_span.text == "Булки"

    def test_sauces_cross(self, driver):
        driver.find_element(*L.SAUCES_TAB).click()
        sauces_span = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.SAUCES_TAB))

        assert sauces_span.text == "Соусы"

    def test_fillings_cross(self, driver):
        driver.find_element(*L.FILLINGS_TAB).click()
        fillings_span = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.FILLINGS_TAB))

        assert fillings_span.text == "Начинки"

