from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators


def test_test_for_logut_of_account(test_login_login_button):
    driver = test_login_login_button

    # Переход в личный кабинет
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    # Ожидание перехода в личный кабинет
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EXIT_BUTTON)
    )

    # Выход из аккаунта
    driver.find_element(*LoginPageLocators.EXIT_BUTTON).click()

    # Проверка, что мы на странице входа
    login_page = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    assert login_page.is_displayed(), "Не удалось выйти из аккаунта."