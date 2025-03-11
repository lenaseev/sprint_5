import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@pytest.mark.parametrize(
    'authorized_driver',
    [
        {'name': 'addddd', 'email': 'elena_sushko_19_216@gmail.com', 'password': 'kkmo43211'},
    ],
    indirect=True
)

def test_successful_registration(authorized_driver): # Регистрация в системе
    driver = authorized_driver
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Ожидание загрузки формы регистрации
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )

    # Проверка, что форма входа отображается
    login_form = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div")
    assert login_form.is_displayed(), "Форма входа отображается после регистрации"

    driver.quit()


@pytest.mark.parametrize(
    'authorized_driver',
    [
        {'name': 'ddddd', 'email': 'elena_sushko_19_211@gmail.com', 'password': '1'},  # Некорректный пароль (короткий)
    ],
    indirect=True
)
def test_registration_with_incorrect_password(authorized_driver): # Проверка на ошибку из-за длины пароля
    driver = authorized_driver

    # Ожидаем появления элемента с ошибкой
    error_message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(@class, 'input__error') and contains(text(), 'Некорректный пароль')]")
        )
    )

    # Получаем текст ошибки
    error_message = error_message_element.text

    assert "Некорректный пароль" in error_message

    driver.quit()


@pytest.mark.parametrize(
    'login_button_xpath',
    [
        "//*[@id='root']/div/main/div/form/button",  # Кнопка входа через «Войти в аккаунт»
        "//*[@id='root']/div/header/nav/a/p",  # Кнопка входа через "Личный кабинет"
    ]
)
def test_log_the_button_personal_account(log_in_using_the_button, login_button_xpath):
    driver = log_in_using_the_button

    # Проверка, что после входа меню конструктора отображается
    login_form = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div")
    assert login_form.is_displayed()

    driver.quit()

def test_login_button_in_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")  # Переход на главную страницу

    # Переход к форме регистрации
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[1]/a").click()

    # Переход к форме входа
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a").click()

    # Ожидание загрузки формы входа
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )

    # Ввод данных для авторизации
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("elena_sushko_19_213@gmail.com")
    driver.find_element(By.NAME, "Пароль").send_keys("kkmo4321")

    # Клик по кнопке входа
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    # Ожидание успешного входа (по появлению элемента после входа)
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p"))
    )

    driver.quit()

def test_login_button_on_password_recovery_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")  # Переход на главную страницу

    # Переход к форме восстановления пароля
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p[2]/a").click()

    # Переход к форме входа
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/div/p/a").click()

    # Ожидание загрузки формы входа
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )

    # Ввод данных для авторизации
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("elena_sushko_19_213@gmail.com")
    driver.find_element(By.NAME, "Пароль").send_keys("kkmo4321")

    # Клик по кнопке входа
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    # Ожидание успешного входа (по появлению элемента после входа)
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p"))
    )

    driver.quit()

