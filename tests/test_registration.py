from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
import time

def test_successful_registration(authorized_driver):
    driver = authorized_driver

    # Проверка, что форма входа отображается
    login_form = driver.find_element(*LoginPageLocators.LOGIN_FORM)
    assert login_form.is_displayed(), "Форма входа не отображается после регистрации"



def test_registration_with_incorrect_password(registration_data_short_password_to):
    driver = registration_data_short_password_to

    # Ожидаем появления элемента с ошибкой
    error_message_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
    )

    # Получаем текст ошибки
    error_message = error_message_element.text

    assert "Некорректный пароль" in error_message, \
        f"Ожидалось сообщение 'Некорректный пароль', но получено: '{error_message}'"
