from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data

#Успешная регистрация
def test_registration(driver):
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()

    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located(L.REGISTER_NAME_INPUT)).send_keys(Data.TEST_NAME)
    wait.until(EC.visibility_of_element_located(L.REGISTER_EMAIL_INPUT)).send_keys(Data.TEST_EMAIL)
    wait.until(EC.visibility_of_element_located(L.REGISTER_PASSWORD_INPUT)).send_keys(Data.TEST_PASSWORD)

    wait.until(EC.element_to_be_clickable(L.REGISTER_SUBMIT_BTN)).click()

    success_message = wait.until(EC.visibility_of_element_located(L.PERSONAL_ACCOUNT_BTN))
    assert success_message.is_displayed()
#Короткий пароль
def test_registration_short_password(driver):
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()
    wait = WebDriverWait(driver, 10)

    wait.until(EC.visibility_of_element_located(L.REGISTER_NAME_INPUT)).send_keys(Data.TEST_NAME)
    wait.until(EC.visibility_of_element_located(L.REGISTER_EMAIL_INPUT)).send_keys(Data.TEST_EMAIL)
    wait.until(EC.visibility_of_element_located(L.REGISTER_PASSWORD_INPUT)).send_keys("123")  

    wait.until(EC.element_to_be_clickable(L.REGISTER_SUBMIT_BTN)).click()

    error_message = wait.until(EC.visibility_of_element_located(L.WRONG_PASSWORD_ERROR))
    assert error_message.is_displayed()
    