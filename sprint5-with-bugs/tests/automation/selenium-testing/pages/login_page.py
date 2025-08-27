# pages/login_page.py
from pages.base_page import BasePage
from pages.utils.locators import LoginPageLocators, CommonLocators
from pages.utils.config import BASE_URL

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BASE_URL}auth/login"

    def load(self):
        self.go_to_url(self.url)

    def google_login(self):
        self.click(LoginPageLocators.GOOGLE_SIGNIN_BUTTON)

    def login(self, email, password):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_SUBMIT_BUTTON)

    def show_password(self):
        self.click(LoginPageLocators.SHOW_PASSWORD_BUTTON)

    def click_register(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
