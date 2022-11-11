### Як запустити тест?

1. Перевірити наявність встановленних залежностей з requirements.txt
2. Перевірити наявність встановленного Appium, відповідного Android приладу/емулятору
3. Зробити тестове підключення
4. Вставити змінні XPATH в файл ../tests/login/test_login.py
5. Запустити Pytest


### Чому код може не працювати?
    В залежності від потужності вашого комп'ютера, буде потрібно змінити час очікування.
    Усі строки коду, де це може бути потрібно, поміченні такими символами:
        # <--------------------


### Корисна інформація
Виконанні завдання:
+    1) Написать базовый функционал для работы с приложением (поиск элемента, клик элемента и тд).
+    2) Написать тест логина пользователя в приложение (позитивный и негативные кейсы).
+    3) Использовать параметризацию.
+    4) Закомитить выполненное задание на гитхаб.

+    1) *Реализовать логирование теста.
-    2) *Реализовать динамическое определение udid телефона через subprocess
+    3) **Написать на проверку элементов SideBar (выезжающее меню слева).


Набір парметрів для негативного тестування:
    Залишити обидва поля порожніми. Натиснути на Вхід. Expected: alert.
    Залишити порожнє поле login. Натиснути на Вхід. Expected: alert.
    Залишити порожнє поле password. Натиснути на Вхід. Expected: alert.
    Ввести коректний логін і некоректний пароль. Expected: alert.
    Ввести некоректний логін, але коректний пароль. Expected: alert.
    У полі логіна ввести коректний пароль, а в полі пароля ввести коректний логін. Expected: alert.

    Ввести скрипт у логін і коректний пароль. Expected: alert.
    Ввести в поле логіна SQL запит. Expected: alert.
    Ввести в поле логіна html-теги. Expected: alert.

    Ввести в поле логіна складну послідовність спецсимволів символів. Expected: alert.

    Ввести в поле логіна і пароля текст, що складається з одних пробілів. Expected: alert.
    Ввести в поле логіна правильний логін, що починається з декількох пробілів, і правильний пароль. Expected: alert.
    Ввести в поле логіна правильний логін, після якого слідують кілька пробілів, і правильний пароль. Expected: alert.

    Ввести коректний логін. Вказати пароль з використанням букв РІЗНОГО регістру. Expected: alert.
    Ввести логін з використанням букв РІЗНОГО регістру. Вказати коректний пароль. Expected: alert.

    Ввести максимально допустиму кількість символів або 4096 у полі логіна. Expected: alert.

    Ввести логін: Login, пароль: Password. Expected: alert.
    Ввести логін і пароль кирилицею. Expected: alert.
    Ввести логін і пароль цифрами. Expected: alert.

    Ввести коректний логін з куточками: <qa.ajax.app.automation@gmail.com> і коректний пароль. Expected: alert.