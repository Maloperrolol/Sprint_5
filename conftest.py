import pytest
from selenium import webdriver
from locators import StellarLocators as L
import time




@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def test_user_credentials():
    return TEST_EMAIL, TEST_PASSWORD, TEST_NAME

@pytest.fixture
def login_helper(driver):
    def _login(email, password):
        driver.find_element(*L.LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*L.LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*L.LOGIN_SUBMIT_BTN).click()
        time.sleep(2)  
    return _login