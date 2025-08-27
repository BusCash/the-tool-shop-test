# tests/test_authentication.py
from pages.utils.locators import CommonLocators, LoginPageLocators, RegisterPageLocators
from pages.homepage import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from faker import Faker  # For generating fake data for registration
import pytest
import time
from selenium.webdriver.support.ui import Select

fake = Faker()


def test_successful_login(browser):
    """Test user can log in with valid credentials."""
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_nav_sign_in()

    login_page = LoginPage(browser)
    login_page.login("customer2@practicesoftwaretesting.com", "welcome01")

    # Assert successful login (e.g., check for logout button, welcome message, or current URL)
    assert home_page.is_element_present(CommonLocators.NAV_SIGN_OUT)


def test_invalid_login(browser):
    """Test user cannot log in with invalid credentials."""
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_nav_sign_in()

    login_page = LoginPage(browser)
    login_page.login("wrong@test.com", "wrong")

    # Assert error message
    assert login_page.is_element_present(LoginPageLocators.LOGIN_ERROR_MESSAGE)


def test_user_registration(browser):
    """Test new user can successfully register."""
    home_page = HomePage(browser)
    home_page.load()
    home_page.click_nav_sign_in()

    login_page = LoginPage(browser)
    login_page.click_register()

    register_page = RegisterPage(browser)
    first_name = fake.first_name()
    last_name = fake.last_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=75)
    dob2 = dob.strftime("%Y-%m-%d")
    dob = dob.strftime("%d-%m-%Y")
    street = fake.street_address()
    postal_code = fake.postcode()
    city = fake.city()
    state = fake.state()
    countries = Select(register_page.find_element(RegisterPageLocators.COUNTRY_SELECT)).options
    # while True:
    #     country = fake.country()
    #     if country in [c.text for c in countries]:
    #         break
    import random
    country = random.choice([c.text for c in countries])
    phone = fake.phone_number()
    import re
    phone = re.sub(r'\D', '', phone)  # Remove non-digit characters
    email = fake.email()
    password = fake.password()

    register_page.register_user(first_name, last_name, dob, dob2, street, postal_code, city, state, country, phone, email, password)

    # Assert successful registration (e.g., success message or redirection to login with pre-filled email)
    assert login_page.is_element_present(LoginPageLocators.LOGIN_FORM)
    login_page.login(email, password)
    assert home_page.is_element_present(CommonLocators.NAV_SIGN_OUT)

