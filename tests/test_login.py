from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для авторизации
def login_flow(driver, email, password):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(L.LOGIN_EMAIL_INPUT)).send_keys(Data.TEST_EMAIL)
    wait.until(EC.visibility_of_element_located(L.LOGIN_PASSWORD_INPUT)).send_keys(Data.TEST_PASSWORD)
    wait.until(EC.element_to_be_clickable(L.LOGIN_SUBMIT_BTN)).click()
    wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_BTN))

# Вход через кнопку 'Войти в аккаунт'
def test_login_for_main(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.LOGIN_IN_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()

# Вход через кнопку "Личный кабинет"
def test_login_from_personal_account(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()

# Вход через форму регистрации
def test_login_from_registration_page(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*L.REGISTER_LINK).click()
    driver.find_element(*L.RESTORE_LOGIN_LINK).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()

# Вход через восстановление пароля
def test_login_from_restore_password(driver):
    email = Data.TEST_EMAIL
    password = Data.TEST_PASSWORD
    driver.get(Data.STELLAR_URL)
    driver.find_element(*L.PERSONAL_ACCOUNT_BTN).click()
    driver.find_element(*L.RESTORE_PASSWORD_LINK).click()
    driver.find_element(*L.RESTORE_LOGIN_LINK).click()
    login_flow(driver, email, password)
    assert driver.find_element(*L.CONSTRUCTOR_BTN).is_displayed()