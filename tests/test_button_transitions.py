from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

def test_button_navigation(test_login_login_button):
    driver = test_login_login_button

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Проверка, что мы на странице личного кабинета
    personal_account_page = driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
    assert personal_account_page.is_displayed(), "Удалось перейти в личный кабинет."

def test_button_navigation(test_login_login_button):
    driver = test_login_login_button

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Переход из личного кабинета в конструктор
    driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click()

    # Проверка, что мы на странице конструктора
    constructor_page = driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON)
    assert constructor_page.is_displayed(), "Не удалось перейти в конструктор."

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Ожидание перехода по лого
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGO_BUTTON)
    )

    # Переход по логотипу
    driver.find_element(*LoginPageLocators.LOGO_BUTTON).click()

    # Проверка, что мы на странице логотипа
    logo_page = driver.find_element(*LoginPageLocators.LOGO_BUTTON)
    assert logo_page.is_displayed(), "Не удалось перейти по логотипу."

def test_button_navigation(test_login_login_button):
    driver = test_login_login_button

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Переход из личного кабинета в конструктор
    driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click()

    # Ожидание перехода по лого
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.CONSTRUCTOR_BUTTON)
    )

    # Переход в раздел "Булки"
    driver.find_element(*LoginPageLocators.BUNS_TAB).click()

    # Проверка, что мы в разделе "Булки"
    buns_page = driver.find_element(*LoginPageLocators.BUNS_TAB)
    assert buns_page.is_displayed(), "Не удалось перейти в раздел Булки."


    # Переход в раздел "Соусы"
    driver.find_element(*LoginPageLocators.SAUCES_TAB).click()

    # Проверка, что мы в разделе "Булки"
    sauses_page = driver.find_element(*LoginPageLocators.SAUCES_TAB)
    assert sauses_page.is_displayed(), "Не удалось перейти в раздел Соусы."


    # Переход в раздел "Начинки"
    driver.find_element(*LoginPageLocators.FILLINGS_TAB).click()

    # Проверка, что мы в разделе "Начинки"
    filling_page = driver.find_element(*LoginPageLocators.FILLINGS_TAB)
    assert filling_page.is_displayed(), "Не удалось перейти в раздел Соусы."


