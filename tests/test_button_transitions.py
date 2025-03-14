from locators import LoginPageLocators
from urls import BASE_URL

# Класс для тестов кнопок и навигации
class TestButtonNavigation:

    def test_button_navigation_to_personal_account(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в личный кабинет
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверка, что мы на странице личного кабинета
        personal_account_page = driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)
        assert personal_account_page.is_displayed(), "Не удалось перейти в личный кабинет."

    def test_button_navigation_to_constructor(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в личный кабинет
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Переход из личного кабинета в конструктор
        driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON).click()

        # Проверка, что мы на странице конструктора
        constructor_page = driver.find_element(*LoginPageLocators.CONSTRUCTOR_BUTTON)
        assert constructor_page.is_displayed(), "Не удалось перейти в конструктор."

    def test_button_navigation_to_logo_page(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в личный кабинет
        driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Переход по логотипу
        driver.find_element(*LoginPageLocators.LOGO_BUTTON).click()

        # Проверка, что мы на странице логотипа
        logo_page = driver.find_element(*LoginPageLocators.LOGO_BUTTON)
        assert logo_page.is_displayed(), "Не удалось перейти по логотипу."


# Класс для тестов навигации по табам
class TestTabNavigation:

    def test_button_navigation_to_buns_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в раздел "Булки"
        driver.find_element(*LoginPageLocators.BUNS_TAB).click()

        # Проверка, что мы в разделе "Булки"
        buns_page = driver.find_element(*LoginPageLocators.BUNS_TAB)
        assert buns_page.is_displayed(), "Не удалось перейти в раздел Булки."

    def test_button_navigation_to_sauces_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в раздел "Соусы"
        driver.find_element(*LoginPageLocators.SAUCES_TAB).click()
        # Проверка, что мы в разделе "Соусы"
        sauses_page = driver.find_element(*LoginPageLocators.SAUCES_TAB)
        assert sauses_page.is_displayed(), "Не удалось перейти в раздел Соусы."

    def test_button_navigation_to_fillings_tab(self, driver):
        # Переход на главную страницу
        driver.get(BASE_URL)

        # Переход в раздел "Начинки"
        driver.find_element(*LoginPageLocators.FILLINGS_TAB).click()

        # Проверка, что мы в разделе "Начинки"
        filling_page = driver.find_element(*LoginPageLocators.FILLINGS_TAB)
        assert filling_page.is_displayed(), "Не удалось перейти в раздел Начинки."