from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def test_test_for_logut_of_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/login")  # Переход на главную страницу

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

    # Переход в личный кабинет
    personal_account_button = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    personal_account_button.click()

    # Ожидаем загрузки страницы личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a"))
    )

    # Проверка, что мы на странице личного кабинета
    personal_account_page = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[1]/a")
    assert personal_account_page.is_displayed(), "Удалось перейти в личный кабинет."

    # Выход из аккаунта
    log_out_button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button")
    log_out_button.click()

