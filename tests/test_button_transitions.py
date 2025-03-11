from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def test_button_navigation():
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

    # Переход из личного кабинета в конструктор
    constructor_button = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
    constructor_button.click()

    # Проверка, что мы на странице конструктора
    constructor_page = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p")
    assert constructor_page.is_displayed(), "Не удалось перейти в конструктор."

    # Переход в раздел «Булки»
    buns_button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
    buns_button.click()

    # Переход в раздел «Соусы»
    sauces_button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span")
    sauces_button.click()

    # Переход в раздел «Начинки»
    fillings_button = driver.find_element(By.XPATH, "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span")
    fillings_button.click()

    # Переход в личный кабинет
    personal_account_button = driver.find_element(By.XPATH, "//*[@id='root']/div/header/nav/a/p")
    personal_account_button.click()

    # Ожидаем загрузки страницы личного кабинета
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/header/nav/a/p"))
    )

    # Переход из личного кабинета по логотипу
    logo_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > header > nav > div > a > svg"))
    )
    logo_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > header > nav > div > a > svg"))
    )

    driver.quit()

