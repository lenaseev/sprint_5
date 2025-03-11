import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def log_in_using_the_button(login_button_xpath):
    # Инициализация WebDriver
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")  # Переход на главную страницу

    # Переход к форме входа
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[2]/div/button").click()

    # Ожидание загрузки формы входа
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='name']"))
    )

    # Ввод данных для авторизации
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys("elena_sushko_19_213@gmail.com")  # Вставьте ваш email
    driver.find_element(By.NAME, "Пароль").send_keys("kkmo4321")  # Вставьте ваш пароль

    # Клик по кнопке входа
    driver.find_element(By.XPATH, login_button_xpath).click()

    # Ожидание успешного входа (по появлению элемента после входа)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p"))
    )

    yield driver

    # Завершение работы драйвера
    #driver.quit()


# Фикстура для авторизации, которая будет использовать разные данные для тестов
@pytest.fixture
def authorized_driver(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Получаем данные для регистрации через параметры
    name = request.param.get('name', 'addddd')
    email = request.param.get('email', 'elena_sushko_19_216@gmail.com')
    password = request.param.get('password', 'kkmo43211')

    # Ввод данных для авторизации
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input").send_keys(name)  # Имя
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input").send_keys(email)  # Email
    driver.find_element(By.NAME, "Пароль").send_keys(password)  # Пароль

    # Клик по кнопке Зарегистрироваться
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    yield driver  # Возвращаем авторизованный драйвер

    # Завершение работы драйвера
    driver.quit()
