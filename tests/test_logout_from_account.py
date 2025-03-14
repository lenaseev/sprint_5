from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import BASE_URL
from test_data import test_user_data

def test_test_for_logut_of_account(driver):
    driver.get(BASE_URL)

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Ожидание загрузки формы входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)
    )

    # Заполнение формы входа
    driver.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(test_user_data["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(test_user_data["password"])

    # Клик по кнопке "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    # Ожидание перехода на главную страницу
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.PLACE_ORDER)
    )

    # Клик по кнопке "Личный кабинет"
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()


    # Ожидание кнопки "Выход"
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(LoginPageLocators.EXIT_BUTTON)
    )

    # Выход из аккаунта
    driver.find_element(*LoginPageLocators.EXIT_BUTTON).click()

    # Проверка, что мы на странице входа
    login_page = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    assert login_page.is_displayed(), "Не удалось выйти из аккаунта."