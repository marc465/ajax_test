from time import sleep
import pytest, logging


logging.basicConfig(filename='logs/log_file.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(funcName)s')


parameters = [
    ['', '', 'Перевірка з порожніми полями'],
    ['', 'qa_automation_password', 'Перевірка з порожнім полем логіна'],
    ['qa.ajax.app.automation@gmail.com', '', 'Перевірка з порожнім полем пароля'],
    ['qa.ajax.app.automation@gmail.com', 'abc', 'Перевірка коректного логіна і некоректного пароля'],
    ['abc', 'qa_automation_password', 'Перевірка коректного пароля і некоректного логіна'],
    ['qa_automation_password', 'qa.ajax.app.automation@gmail.com', 'Перевірка на поміняти місцями коректні пароль і логін'],
    
    ['print("Hello, World!")', 'abc', 'Перевірка роботи зі скриптом'],
    ['SELECT * FROM table', 'abc', 'Перевірка роботи з SQL запитом'],
    ['<body><p>Hello, World</p></body>', 'abc', 'Перевірка роботи з html-тегами'],

    ['/n/r//.,:"!@#$%^&*()-+~', '/n/r//.,:"!@#$%^&*()-+~', 'Перевірка роботи зі спецсимволами'],

    ['     ', '     ', 'Перевірка на роботу з пробілами'],
    ['qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'Перевірка на роботу з пробілами на початку рядка'],
    ['qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'Перевірка на роботу з пробілами в кінці рядка'],
    
    ['qA.AjaX.APP.autOmation@GmaiL.coM', 'qa_automation_password', 'Перевірка на роботу з різним регістром (логін)'],
    ['qa.ajax.app.automation@gmail.com', 'Qa_aUToMAtioN_pasSwoRd', 'Перевірка на роботу з різним регістром (пароль)'],
    
    ['qa.ajax.app.automation'*128, 'qa_automation_password__password'*128, 'Перевірка на максимальну кількість символів'],
    
    ['Login', 'Password', 'Перевірка на роботу з латинськими літерами'],
    ['Логін', 'Пароль', 'Перевірка на роботу з буквами кирилиці'],
    ['123', '123', 'Перевірка на роботу з цифрами'],

    ['<qa.ajax.app.automation@gmail.com>', 'qa_automation_password', 'Перевірка на обрамлений <> логін']
]
parameters2 = ['qa.ajax.app.automation@gmail.com', 'qa_automation_password']


"""
Вирішив не заповнювати змінні з XPATH-ом, щоб ненароком не зіпсувати тест 
"""


login_field = ''
password_field = ''
login_buttom = ''

home_page_element = ''

sidebar = ''
sidebar_element = ''


@pytest.fixture(params=parameters)
def negative_params(request):
    """
    Повертає один набір параметрів зі списку
    """
    return request.param


def test_user_login_negative_case(user_login_fixture, negative_params):

    """
    Запрошує у negative_params один набір параметрів,
    Вставляє в поле логіна тестові дані,
    Вставляє в поле пароля тестові дані,
    Натискає на кнопку Увійти,
    Чекає,

    ***Через технічні проблеми і погане з'єднання,
    було вирішено не шукати на сторінці повідомлення Не всі заповнені поля, Некоректне введення тощо
    ***

    Вважаємо, що тест пройшов успішно, якщо після очікування ми залишилися на сторінці входу
    """

    try:
        logging.info('Починаю тестування: {0}'.format(negative_params[2]))
        elem = user_login_fixture.find_element(login_field)
        user_login_fixture.input_data(elem, negative_params[0])

        elem = user_login_fixture.find_element(password_field)
        user_login_fixture.input_data(elem, negative_params[1])

        user_login_fixture.click_element(login_buttom)

        sleep(5) # <--------------------

        assert user_login_fixture.is_element_there(login_field)

    except Exception as e:
        logging.error('Виникла помилка під час тестування: {0}'.format(negative_params[2]))
        logging.exception(e)
        raise Exception('Виникла помилка')                  # Викликаємо помилку, щоб тест був позначенний як Failed


def test_user_login_positive_case(user_login_fixture):
    """
    Вводимо коректні логін і пароль,
    Натискаємо ввести,
    Чекаємо,
    Вважаємо, що тест пройшов успішно, якщо знаходимо елемент домашньої сторінки користувача
    """

    try:
        logging.info('Починаю тестування позитивного кейсу')
        elem = user_login_fixture.find_element(login_field)
        user_login_fixture.input_data(elem, parameters2[0])

        elem = user_login_fixture.find_element(password_field)
        user_login_fixture.input_data(elem, parameters2[1])

        user_login_fixture.click_element(login_buttom)

        sleep(5) # <--------------------

        assert user_login_fixture.is_element_there(home_page_element)

    except Exception as e:
        logging.error('Виникла помилка під час тестування позитивного кейсу')
        logging.exception(e)
        raise Exception('Виникла помилка')                  # Викликаємо помилку, щоб тест був позначенний як Failed


def test_sidebar(user_login_fixture):
    """
    Заходимо в акаунт,
    Викликаємо бічне меню,
    Шукаємо елементи в ньому,
    Вважаємо, що тест пройшов успішно, якщо елемент бічного меню знайден
    """
    
    try:
        elem = user_login_fixture.find_element(login_field)
        user_login_fixture.input_data(elem, parameters2[0])

        elem = user_login_fixture.find_element(password_field)
        user_login_fixture.input_data(elem, parameters2[1])

        user_login_fixture.click_element(login_buttom)

        sleep(5)
        
        user_login_fixture.click_element(sidebar)

        sleep(3)

        assert user_login_fixture.is_element_there(sidebar_element)
    
    except Exception as e:
        logging.error('Виникла помилка під час тестування позитивного кейсу')
        logging.exception(e)
        raise Exception('Виникла помилка')                  # Викликаємо помилку, щоб тест був позначенний як Failed
