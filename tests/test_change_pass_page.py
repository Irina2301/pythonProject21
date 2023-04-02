import pytest
from pages.change_pass_page import ChangePassPage
from settings import url_change_page


class TestChangePassPage():
    # тест на проверку типа восстановления пароля по умолчанию
    def test_default_password_recovery_type(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.default_password_recovery_type()

    @pytest.mark.xfail
    # тест на проверку работы поля ввода номера телефона (ввод валидного номера)
    def test_phone_field_validation_valid_data(self, browser):
        """ Поле принимает 11-значное число в случае если первая цифра 3, 7 или 8.
        В остальных случаях поле принимает 10-значное число """
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.phone_field_validation_valid_data()

    # тест на проверку работы поля ввода email(ввод валидного email)
    def test_email_field_validation_valid_data(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.email_field_validation_valid_data()

    # тест на проверку работы кнопки формы авторизации
    def test_go_back_button(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.go_back_button()

    # тест на проверку работы ссылки на страницу с пользовательским соглашением в футере
    def test_link_fut_to_the_user_agreement_page(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.link_to_the_user_agreement_page()

    # тест на проверку восстановления пароля с незаполненными полями
    def test_password_recovery_with_empty_fields(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_empty_fields()

    # тест на проверку восстановления пароля с незаполненным значением капчи
    def test_password_recovery_with_empty_captcha(self, browser):
        change_pass_page = ChangePassPage(browser, url_change_page)
        change_pass_page.open()
        change_pass_page.password_recovery_with_empty_fields()

