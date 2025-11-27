import time
from locators import StellarLocators as L
from data import Data

#Успешная регистрация
def test_seccess_registration(driver, test_user_credentials):
    email, password, name = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()
    driver.find_element(*L.REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*L.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.REGISTER_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*L.REGISTER_SUBMIT_BTN).click()
    time.sleep(2)  
    assert driver.find_element(*L.PERSONAL_ACCOUNT_BTN).is_displayed()
#Короткий пароль
def test_wrong_password_registration(driver, test_user_credentials):
    email, password, name = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()
    driver.find_element(*L.REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*L.REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*L.REGISTER_PASSWORD_INPUT).send_keys("123")
    driver.find_element(*L.REGISTER_SUBMIT_BTN).click()
    time.sleep(2)  
    assert driver.find_element(*L.WRONG_PASSWORD_ERROR).is_displayed()
    