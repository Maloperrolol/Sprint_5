from selenium.webdriver.chrome.webdriver import WebDriver
from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Проверка работы вкладок конструктора
class TestConstructorTabs:

    def test_go_to_buns_section(self, driver):
        driver.get(Data.STELLAR_URL)
        driver.find_element(*L.SAUCES_TAB).click()
        driver.find_element(*L.BUNS_TAB).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Булки"))
        assert driver.find_element(*L.ACTIVE_TAB).text == "Булки"

    def test_go_to_sauces_section(self, driver):
        driver.get(Data.STELLAR_URL)
        driver.find_element(*L.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Соусы"))
        assert driver.find_element(*L.ACTIVE_TAB).text == "Соусы"

    def test_go_to_fillings_section(self, driver):
        driver.get(Data.STELLAR_URL)
        driver.find_element(*L.FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Начинки"))
        assert driver.find_element(*L.ACTIVE_TAB).text == "Начинки"

