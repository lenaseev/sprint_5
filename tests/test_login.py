from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import BASE_URL, REGISTER_URL, FORGOT_PASSWORD
from test_data import test_user_data


class TestLogin:

    def test_login_from_base_url_with_login_button(self, driver):
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

        # Ожидание появления кнопки "Оформить заказ"
        place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

        # Проверка, что кнопка "Оформить заказ" отображается
        assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"

    def test_login_from_base_url_with_personal_account_button(self, driver):
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

        # Ожидание появления кнопки "Оформить заказ"
        place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

        # Проверка, что кнопка "Оформить заказ" отображается
        assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"

    def test_login_from_login_url_with_register_button(self, driver):
        # Переход на страницу регистрации
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

        # Ожидание появления кнопки "Оформить заказ"
        place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

        # Проверка, что кнопка "Оформить заказ" отображается
        assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"

    def test_login_from_login_url_with_recover_password_button(self, driver):
        # Переход на страницу восстановления пароля
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

        # Ожидание появления кнопки "Оформить заказ"
        place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

        # Проверка, что кнопка "Оформить заказ" отображается
        assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"