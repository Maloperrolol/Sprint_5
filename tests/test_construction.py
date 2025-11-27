from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Проверка работы вкладок конструктора
def test_constructor_tabs(driver):
    driver.get(Data.STELLAR_URL)
    
    wait = WebDriverWait(driver, 5)

    driver.find_element(*L.SAUCES_TAB).click()
    wait.until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Соусы"))
    assert driver.find_element(*L.ACTIVE_TAB).text == 'Соусы'

    driver.find_element(*L.FILLINGS_TAB).click()
    wait.until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Начинки"))
    assert driver.find_element(*L.ACTIVE_TAB).text == 'Начинки'

    driver.find_element(*L.BUNS_TAB).click()
    wait.until(EC.text_to_be_present_in_element(L.ACTIVE_TAB, "Булки"))
    assert driver.find_element(*L.ACTIVE_TAB).text == 'Булки'