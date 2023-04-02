Финальный проект по 28 модулю.
python -m pytest -v --driver Chrome --driver-path C:\Users\Lenovo\Downloads\chromedriver.exe tests\ - запуск тестов
В папке pages в файле base_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.
В папке pages в файлах auth_page.py, change_pass_page.py, reg_page.py находятся методы проверок: файл auth_page.py содержит методы проверок формы авторизации; файл change_pass_page.py содержит методы проверок формы восстановления пароля; файл reg_page.py содержит методы проверок формы регистрации.
В папке tests в файлах test_auth_page.py, test_change_pass_page.py, test_reg_page.py находятся тесты.
В папке pages в файле "locators.py находятся все локаторы.
В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера.
В корне проекта в файле settings.py находятся методы и переменные для параметризации тестов.
