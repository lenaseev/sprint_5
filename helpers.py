import random
import string

def generate_unique_email(domain="ya.ru"):
    """
    Генерирует уникальный email в формате логин@домен.
    :param domain: Домен email (по умолчанию "ya.ru").
    :return: Уникальный email.
    """
    # Генерация случайного логина
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    # Формируем email
    return f"{login}@{domain}"