from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кнопка "Войти"
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт" ок
    EMAIL_FIELD = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']")  # ок
    PASSWORD_FIELD = (By.NAME, "Пароль")  # ок
    LOGIN_FORM = (By.XPATH, "//*[@id='root']/div/main/div")
    PLACE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Оформить заказ ок
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # ок
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # ок
    RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")  # ок
    BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_FROM_REGISTER = (
        By.XPATH, "//a[@href='/login' and contains(text(), 'Войти')]")  # Войти после кнопки регистрации ок
    CONSTRUCTOR_BUTTON = (By.XPATH, "// p[contains(text(), 'Конструктор')]")
    EXIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    LOGO_BUTTON = (By.XPATH, "//a[@href='/']")
    BUNS_TAB = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
class HeaderLocators:
    USER_PROFILE = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")

class RegisterPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR,
                    "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")  # Кнопка "Войти"
    NAME_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input")
    LOGIN_TO_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка "Войти в аккаунт" ок
    EMAIL_FIELD = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input")  # ок
    PASSWORD_FIELD = (By.NAME, "Пароль")  # ок
    LOGIN_FORM = (By.XPATH, "//*[@id='root']/div/main/div")
    PLACE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")  # Оформить заказ ок
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")  # ок
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # ок
    RECOVER_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")  # ок
    BURGER_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    LOGIN_FROM_REGISTER = (
    By.XPATH, "//a[@href='/login' and contains(text(), 'Войти')]")  # Войти после кнопки регистрации ок
    CONSTRUCTOR_BUTTON = (By.XPATH, "// p[contains(text(), 'Конструктор')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Локатор для сообщения