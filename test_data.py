
from helpers import generate_unique_email

# Модуль с тестовыми данными
test_user_data = {
    'email': 'elena_sushko_19_213@gmail.com',
    'password': 'kkmo4321'
}

test_registration_data = {
    'name': 'addddd',
    'email': generate_unique_email(),
    'password': 'kkmo43211'
}

test_registration_data_short_password = {
    'name': 'addddd',
    'email': generate_unique_email(),
    'password': '123'
}