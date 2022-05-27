from .base_page import BasePage
from .locators import LoginPageLocatore


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocatore.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_pwd = self.browser.find_element(*LoginPageLocatore.REGISTER_PASSWORD1)
        input_pwd.send_keys(password)
        repeat_pwd = self.browser.find_element(*LoginPageLocatore.REGISTER_PASSWORD2)
        repeat_pwd.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocatore.REGISTER_SUBMIT)
        register_btn.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #проверка на корректность url адреса
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login link is incorrect"

    #проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocatore.LOGIN_FORM), "Login form is not presented"

    #проверка, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocatore.REGISTER_FORM), "Register form is not presented"