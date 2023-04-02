from settings import valid_phone, valid_email
from .base_page import BasePage
from .locators import AuthPageLocators, ChangePassPageLocators, UserAgreementPageLocators, \
    RejectedRequestPageLocators, BaseLocators


class ChangePassPage(BasePage):
    # метод проверки типа восстановления пароля по умолчанию
    def default_password_recovery_type(self):
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_PLACEHOLDER_TELEPHONE), \
            "element not found"

    # метод проверки на валидацию поля ввода номера телефона (ввод валидного номера)
    def phone_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        phone = valid_phone()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(phone)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert ("7"+str(phone)) == value, "phone do not match"

    # метод проверки на валидацию поля ввода email(ввод валидного email)
    def email_field_validation_valid_data(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_MAIL).click()
        username_input = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT)
        email = valid_email()
        username_input.send_keys(email)
        self.find_element(BaseLocators.BODY).click()
        element = self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT_VALUE)
        value = element.get_attribute("value")
        assert email == value, "email do not match"

    # метод проверки работы кнопки формы авторизации
    def go_back_button(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_GO_BACK_BUTTON).click()
        assert self.is_element_present(AuthPageLocators.AUTH_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/authenticate" in self.browser.current_url, \
            "url do not match"

    # метод проверки работы ссылки на страницу с пользовательским соглашением в футере
    def link_to_the_user_agreement_page(self):
        original_window = self.browser.current_window_handle
        assert len(self.browser.window_handles) == 1
        self.find_element(ChangePassPageLocators.CHANGE_PASS_PRIVACY_POLICY_LINK).click()
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
            else:
                pass
        assert self.is_element_present(UserAgreementPageLocators.USER_AGREEMENT_HEADING), "element not found"
        assert "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html" in self.browser.current_url, \
            "url do not match"

    # метод проверки восстановления пароля с незаполненными полями
    def password_recovery_with_empty_fields(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_PHONE).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_ERROR_ENTER_PHONE_NUMBER), \
            "element not found"

    # метод проверки восстановления пароля с незаполненным значением капчи
    def password_recovery_with_empty_captcha(self):
        self.find_element(ChangePassPageLocators.CHANGE_PASS_TAB_MAIL).click()
        self.find_element(ChangePassPageLocators.CHANGE_PASS_USERNAME_INPUT).send_keys(valid_email())
        self.find_element(ChangePassPageLocators.CHANGE_PASS_CONTINUE_BUTTON).click()
        assert "https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials" \
               in self.browser.current_url, "url do not match"
        assert self.is_element_present(ChangePassPageLocators.CHANGE_PASS_ERROR_INVALID_USERNAME_OR_TEXT), \
            "element not found"

