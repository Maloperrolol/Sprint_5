from locators import StellarLocators as L
from data import Data
import time

def login_flow(driver, email, password):
    driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(Data.TEST_EMAIL)
    driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(Data.TEST_PASSWORD)
    driver.find_element(*L.LOGIN_SUBMIT_BTN).click()
    time.sleep(1)
#Вход через кнопку 'Войти в аккаунт'
def test_login_for_main(driver, test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed
#Вход через кнопку "Личный кабинет"
def test_login_from_personal_account(driver, test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()
#Вход через форму регистрации
def test_login_from_registration_page(driver, test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()
    driver.find_element(*L.RESTORE_LOGIN_LINK).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()
#Вход через востановление пароля
def test_login_from_restore_password(driver, test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*L.RESTORE_PASSWORD_LINK).click()
    driver.find_element(*L.RESTORE_LOGIN_LINK).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()