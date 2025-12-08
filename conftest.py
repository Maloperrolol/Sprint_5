import pytest
from selenium import webdriver
from locators import StellarLocators as L
from data import Data
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def login_helper(driver):
    def _login(email, password):
        driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.LOGIN_SUBMIT_BTN).click()
        time.sleep(2)  
    return _login

def login_flow(driver, email, password):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(L.LOGIN_EMAIL_INPUT)).send_keys(Data.TEST_EMAIL)
    wait.until(EC.visibility_of_element_located(L.LOGIN_PASSWORD_INPUT)).send_keys(Data.TEST_PASSWORD)
    wait.until(EC.element_to_be_clickable(L.LOGIN_SUBMIT_BTN)).click()
    wait.until(EC.visibility_of_element_located(L.CONSTRUCTOR_BTN))