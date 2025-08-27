# pages/register_page.py
from pages.base_page import BasePage
from pages.utils.locators import RegisterPageLocators, CommonLocators
from pages.utils.config import BASE_URL
from selenium.webdriver.support.ui import Select

class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{BASE_URL}auth/register"

    def load(self):
        self.go_to_url(self.url)

    def register_user(self, first_name, last_name, dob, dob2, street, postal_code, city, state, country, phone, email, password):
        self.type_text(RegisterPageLocators.FIRST_NAME_INPUT, first_name)
        self.type_text(RegisterPageLocators.LAST_NAME_INPUT, last_name)
        self.type_text(RegisterPageLocators.DOB_INPUT, dob)
        print(self.find_element(RegisterPageLocators.DOB_INPUT).get_attribute("value"))
        if self.find_element(RegisterPageLocators.DOB_INPUT).get_attribute("value") != dob2:
            self.find_element(RegisterPageLocators.DOB_INPUT).send_keys(dob2)
        print(self.find_element(RegisterPageLocators.DOB_INPUT).get_attribute("value"))
        # self.driver.execute_script("arguments[0].value = arguments[1];", self.find_element(RegisterPageLocators.DOB_INPUT), dob)
        self.type_text(RegisterPageLocators.STREET_INPUT, street)
        self.type_text(RegisterPageLocators.POSTAL_CODE_INPUT, postal_code)
        self.type_text(RegisterPageLocators.CITY_INPUT, city)
        self.type_text(RegisterPageLocators.STATE_INPUT, state)
        Select(self.find_element(RegisterPageLocators.COUNTRY_SELECT)).select_by_visible_text(country)
        self.type_text(RegisterPageLocators.PHONE_INPUT, phone)
        self.type_text(RegisterPageLocators.EMAIL_INPUT, email)
        self.type_text(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click(RegisterPageLocators.REGISTER_SUBMIT_BUTTON)
        