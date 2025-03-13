from locators import LoginPageLocators

def test_login_from_base_url_with_login_button(test_login_login_button):
    driver = test_login_login_button

    # Ожидание появления кнопки "Оформить заказ"
    place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

    # Проверка, что кнопка "Оформить заказ" отображается
    assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"


def test_login_from_base_url_with_personal_account_button(test_login_personal_acc_button):
    driver = test_login_personal_acc_button

    # Ожидание появления кнопки "Оформить заказ"
    place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

    # Проверка, что кнопка "Оформить заказ" отображается
    assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"



def test_login_from_login_url_with_register_button(test_login_register_button):
     driver = test_login_register_button

     # Ожидание появления кнопки "Оформить заказ"
     place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

     # Проверка, что кнопка "Оформить заказ" отображается
     assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"


def test_login_from_login_url_with_recover_password_button(test_login_forgot_password):
    driver = test_login_forgot_password

    # Ожидание появления кнопки "Оформить заказ"
    place_order_button = driver.find_element(*LoginPageLocators.PLACE_ORDER)

    # Проверка, что кнопка "Оформить заказ" отображается
    assert place_order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после успешного входа"


