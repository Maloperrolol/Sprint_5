from selenium.webdriver.common.by import By

class StellarLocators:
    #Главная страница
    LOGIN_IN_ACCOUNT_BTN = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")
    #Регистрация
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    REGISTER_NAME_INPUT = (By.NAME, "name")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//*[@class='text input__textfield text_type_main-default']")
    REGISTER_PASSWORD_INPUT = (By.NAME, "Пароль")
    REGISTER_SUBMIT_BTN = (By.XPATH, "//button[text()='Зарегистрироваться']")
    WRONG_PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    #Вход
    LOGIN_EMAIL_INPUT = (By.XPATH, "//*[@class='text input__textfield text_type_main-default']")
    LOGIN_PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_SUBMIT_BTN = (By.XPATH, "//button[text()='Войти']")
    #Восстановление пароля
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    RESTORE_LOGIN_LINK = (By.LINK_TEXT, "Войти")
    #Личный кабинет
    EXIT_BTN = (By.XPATH, "//button[text()='Выход']")
    #Конструктор
    CONSTRUCTOR_BTN = (By.LINK_TEXT, "Конструктор")
    LOGO_BTN = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    ACTIVE_TAB = (By.CSS_SELECTOR, "[class*='tab_tab_type_current']")