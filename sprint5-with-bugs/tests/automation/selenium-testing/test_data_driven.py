from pages.utils.locators import CommonLocators, LoginPageLocators, RegisterPageLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import pytest
import time
from selenium.webdriver.support.ui import Select
import csv

data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    i = 0
    for row in reader:
        data.append(pytest.param(*row, id=str(i)))
        i += 1

print(data)


# data will be a list of lists, where each inner list is a row from the CSV
@pytest.mark.parametrize(
    "first_name, last_name, date_of_birth, address, postcode, city, state, phone_number, email, password", data)
def test_bulk_user_registration(browser, first_name, last_name, date_of_birth, address, postcode, city, state,
                                phone_number, email, password):
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_nav_sign_in()

    login_page = LoginPage(browser)
    login_page.click_register()

    register_page = RegisterPage(browser)
    dob = date_of_birth
    countries = Select(register_page.find_element(RegisterPageLocators.COUNTRY_SELECT)).options
    import random
    country = random.choice([c.text for c in countries])
    import re
    phone = re.sub(r'\D', '', phone_number)
    register_page.register_user(first_name, last_name, dob, dob, address, postcode, city, state, country, phone,
                                email, password)

    # Assert successful registration (e.g., success message or redirection to login with pre-filled email)
    assert login_page.is_element_present(LoginPageLocators.LOGIN_FORM)
    login_page.login(email, password)
    assert home_page.is_element_present(CommonLocators.NAV_SIGN_OUT)
