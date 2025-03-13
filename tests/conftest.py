import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email
from urls import LOGIN_URL, REGISTER_URL, BASE_URL, FORGOT_PASSWORD
from locators import LoginPageLocators, HeaderLocators, RegisterPageLocators
from test_data import test_user_data, test_registration_data, test_registration_data_short_password

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    # Используем фиксированные данные для успешной регистрации
    registration_data = {
        'name': 'addddd',
        'email': generate_unique_email(),
        'password': 'kkmo43211'
    }

    # Переход на страницу регистрации
    driver.get(REGISTER_URL)

    # Ожидание загрузки формы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_FIELD)
    )

    # Ввод данных для регистрации
    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(registration_data['name'])
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(registration_data['email'])
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(registration_data['password'])

    # Клик по кнопке "Зарегистрироваться"
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    # Ожидание перехода на страницу входа после успешной регистрации
    WebDriverWait(driver, 10).until(
        EC.url_to_be(LOGIN_URL)
    )

    yield driver

@pytest.fixture
def registration_data_short_password_to(driver):
    # Используем глобальные данные для регистрации с коротким паролем
    registration_data = {
        'name': 'addddd',
        'email': generate_unique_email(),
        'password': '123'
    }

    # Переход на страницу регистрации
    driver.get(REGISTER_URL)

    # Ожидание загрузки формы регистрации
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(RegisterPageLocators.NAME_FIELD)
    )

    # Ввод данных для регистрации
    driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(registration_data['name'])
    driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(registration_data['email'])
    driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(registration_data['password'])

    # Клик по кнопке "Зарегистрироваться"
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    yield driver

@pytest.fixture
def test_login_login_button(driver):
    # Переход на главную страницу
    driver.get(BASE_URL)

    # Ожидание загрузки кнопки "Войти в аккаунт"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_TO_ACCOUNT)
    )

    # Клик по кнопке "Войти в аккаунт"
    driver.find_element(*LoginPageLocators.LOGIN_TO_ACCOUNT).click()

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

    # Возвращаем драйвер для использования в тестах
    yield driver

@pytest.fixture
def test_login_personal_acc_button(driver):
    # Переход на главную страницу
    driver.get(BASE_URL)

    # Ожидание загрузки кнопки "Личный кабинет"
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
    )

    # Клик по кнопке "Личный кабинет"
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

    # Возвращаем драйвер для использования в тестах
    yield driver

@pytest.fixture
def test_login_register_button(driver):
    # Переход на главную страницу
    driver.get(REGISTER_URL)

    # Клик по кнопке "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_FROM_REGISTER).click()

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

    # Возвращаем драйвер для использования в тестах
    yield driver

@pytest.fixture
def test_login_forgot_password(driver):
    # Переход на главную страницу
    driver.get(FORGOT_PASSWORD)

    # Клик по кнопке "Войти"
    driver.find_element(*LoginPageLocators.LOGIN_FROM_REGISTER).click()

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

    # Возвращаем драйвер для использования в тестах
    yield driver