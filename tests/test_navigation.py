import pytest
from locators import StellarLocators as L  
from data import Data
from tests.test_login import login_flow
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Переход в Личный кабинет
def test_go_to_personal_account(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.LOGIN_IN_ACCOUNT_BTN)).click()

    login_flow(driver, Data.TEST_EMAIL, Data.TEST_PASSWORD)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.PERSONAL_ACCOUNT_BTN)).click()

    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.EXIT_BTN)).is_displayed()


# Переход из личного кабинета в конструктор
def test_go_to_construction_from_personal_account(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.LOGIN_IN_ACCOUNT_BTN)).click()
    login_flow(driver, Data.TEST_EMAIL, Data.TEST_PASSWORD)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.PERSONAL_ACCOUNT_BTN)).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.CONSTRUCTOR_BTN)).click()

    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.BUNS_TAB)).is_displayed()


# Переход на логотип Stellar Burgers
def test_go_to_logo_from_personal_account(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.LOGIN_IN_ACCOUNT_BTN)).click()
    

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.PERSONAL_ACCOUNT_BTN)).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.LOGO_BTN)).click()

    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.BUNS_TAB)).is_displayed()


# Выход из аккаунта
def test_go_exit_from_personal_account(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.LOGIN_IN_ACCOUNT_BTN)).click()
    login_flow(driver, Data.TEST_EMAIL, Data.TEST_PASSWORD)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.PERSONAL_ACCOUNT_BTN)).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(L.EXIT_BTN)).click()

    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(L.REGISTER_LINK)).is_displayed()