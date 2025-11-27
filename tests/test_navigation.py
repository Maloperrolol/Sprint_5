import pytest
from locators import StellarLocators as L
from conftest import TEST_EMAIL, TEST_PASSWORD
import time
from data import Data
from tests.test_login import login_flow

#Переход в Личный кабинет
def test_go_to_personal_account(driver,test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    time.sleep(4)
    assert driver.find_element(*L.EXIT_BTN).is_displayed()
#Переход из личного кабинет в конструктор
def test_go_to_construction_from_personal_account(driver,test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    time.sleep(4)
    driver.find_element(*L.CONSTRUCTOR_BTN).click()
    time.sleep(4)
    assert driver.find_element(*L.BUNS_TAB).is_displayed()

#Переход на логотип Stellar Burgers
def test_go_to_logo_from_personal_account(driver,test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    time.sleep(4)
    driver.find_element(*L.LOGO_BTN).click()
    assert driver.find_element(*L.BUNS_TAB).is_displayed()
    
#Выход из аккаунта
def test_go_exit_from_personal_account(driver,test_user_credentials):
    email, password, _ = test_user_credentials
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    time.sleep(4)
    driver.find_element(*L.EXIT_BTN).click()
    time.sleep(4)
    assert driver.find_element(*L.REGISTER_LINK).is_displayed()