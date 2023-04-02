from pages.auth_page import AuthPage
from settings import url_base_page

class TestAuthPage():
    # тест на проверку открытия формы авторизации
    def test_the_authorization_form_is_open(self, browser):
        auth_page.open()
        auth_page = AuthPage(browser, url_base_page)
        auth_page.the_authorization_form_is_open()

    # тест на проверку наличия логотипа и слогана
    def test_availability_of_the_logo_and_slogan(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.availability_of_the_logo_and_slogan()

    # тест на проверку наличия меню выбора типа аутентификации
    def test_availability_of_the_tab_menu(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.availability_of_the_tab_menu()

    # тест на проверку типа аутентификации по умолчанию
    def test_default_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.default_authentication_type()

    # тест на проверку автоматического изменения типа аутентификации
    def test_automatic_change_of_authentication_type(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.automatic_change_of_authentication_type()

    # тест на проверку ссылки на форму восстановления пароля
    def test_link_to_the_password_recovery_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_password_recovery_form()

    # тест на проверку ссылки на форму регистрации
    def test_link_to_the_registration_form(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_registration_form()

    # тест на проверку ссылки под кнопкой "Войти" на страницу с пользовательским соглашением
    def test_link_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_the_user_agreement_page()

    # тест на проверку ссылки в футере на страницу с пользовательским соглашением
    def test_link_fut_to_the_user_agreement_page(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_fut_to_the_user_agreement_page()

    # тест на проверку ссылки на страницу авторизации при нажатии кнопки "ВКонтакте"
    def test_link_to_social_vk(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.link_to_social_vk()

    # тест на проверку авторизации с незаполненными полями
    def test_authorization_with_empty_fields(self, browser):
        auth_page = AuthPage(browser, url_base_page)
        auth_page.open()
        auth_page.authorization_with_empty_fields()



