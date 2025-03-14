from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
from test_data import test_registration_data, test_registration_data_short_password
from urls import LOGIN_URL, REGISTER_URL
class TestRegistration:


    def test_successful_registration(self, driver):

        driver.get(REGISTER_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegisterPageLocators.NAME_FIELD)
        )
        driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(test_registration_data['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(test_registration_data['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(test_registration_data['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Проверка, что форма входа отображается после успешной регистрации
        login_form = driver.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form.is_displayed(), "Форма входа не отображается после регистрации"

    def test_registration_with_incorrect_password(self, driver):

        driver.get(REGISTER_URL)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegisterPageLocators.NAME_FIELD)
        )
        driver.find_element(*RegisterPageLocators.NAME_FIELD).send_keys(test_registration_data_short_password['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_FIELD).send_keys(test_registration_data_short_password['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_FIELD).send_keys(test_registration_data_short_password['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        # Ожидаем появления сообщения об ошибке
        error_message_element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
        )
        error_message = error_message_element.text
        assert "Некорректный пароль" in error_message, \
            f"Ожидалось сообщение 'Некорректный пароль', но получено: '{error_message}'"