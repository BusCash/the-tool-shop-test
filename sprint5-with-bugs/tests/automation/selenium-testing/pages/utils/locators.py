# utils/locators.py
from selenium.webdriver.common.by import By

class CommonLocators:
    # Generic locators that might appear on multiple pages
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.toast-success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.toast-error")
    BUG_MESSAGE = (By.CSS_SELECTOR, "div.toast")  # with-bugs version

    # Nav bars locators
    LOGO = (By.CSS_SELECTOR, "a.navbar-brand")
    MENU = (By.CSS_SELECTOR, "button.navbar-toggler")
    NAV_HOME = (By.CSS_SELECTOR, "a[data-test='nav-home']")
    NAV_CATEGORIES = (By.CSS_SELECTOR, "a[data-test='nav-categories']")
    NAV_HAND_TOOLS = (By.CSS_SELECTOR, "a[data-test='nav-hand-tools']")
    NAV_POWER_TOOLS = (By.CSS_SELECTOR, "a[data-test='nav-power-tools']")
    NAV_OTHER = (By.CSS_SELECTOR, "a[data-test='nav-other']")
    NAV_SPECIAL_TOOLS = (By.CSS_SELECTOR, "a[data-test='nav-special-tools']")
    NAV_RENTALS = (By.CSS_SELECTOR, "a[data-test='nav-rentals']")
    NAV_CONTACT = (By.CSS_SELECTOR, "a[data-test='nav-contact']")
    NAV_SIGN_IN = (By.CSS_SELECTOR, "a[data-test='nav-sign-in']")
    NAV_CART = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    NAV_CART_QUANTITY = (By.CSS_SELECTOR, "span[data-test='nav-cart-quantity']")
    LANGUAGE_SELECT = (By.CSS_SELECTOR, "button[data-test='language-select']")
    LANG_DE = (By.CSS_SELECTOR, "a[data-test='lang-de']")
    LANG_EN = (By.CSS_SELECTOR, "a[data-test='lang-en']")
    LANG_ES = (By.CSS_SELECTOR, "a[data-test='lang-es']")
    LANG_FR = (By.CSS_SELECTOR, "a[data-test='lang-fr']")
    LANG_NL = (By.CSS_SELECTOR, "a[data-test='lang-nl']")
    LANG_TR = (By.CSS_SELECTOR, "a[data-test='lang-tr']")

    # After login
    NAV_MENU = (By.CSS_SELECTOR, "a[data-test='nav-menu']")
    NAV_MY_ACCOUNT = (By.CSS_SELECTOR, "a[data-test='nav-my-account']")
    NAV_MY_FAVORITES = (By.CSS_SELECTOR, "a[data-test='nav-my-favorites']")
    NAV_MY_PROFILE = (By.CSS_SELECTOR, "a[data-test='nav-my-profile']")
    NAV_MY_INVOICES = (By.CSS_SELECTOR, "a[data-test='nav-my-invoices']")
    NAV_MY_MESSAGES = (By.CSS_SELECTOR, "a[data-test='nav-my-messages']")
    NAV_SIGN_OUT = (By.CSS_SELECTOR, "a[data-test='nav-sign-out']")

    # Add other common elements like navigation bars, headers, footers if needed

class HomePageLocators: # And CategoriesPageLocators:
    # Sort
    SORT_SELECT = (By.CSS_SELECTOR, "select[data-test='sort']")
    SORT_OPTION = (By.CSS_SELECTOR, "option[value='']") # Default option
    SORT_NAME_ASC_OPTION = (By.CSS_SELECTOR, "option[value='name,asc']")
    SORT_NAME_DESC_OPTION = (By.CSS_SELECTOR, "option[value='name,desc']")
    SORT_PRICE_ASC_OPTION = (By.CSS_SELECTOR, "option[value='price,asc']")
    SORT_PRICE_DESC_OPTION = (By.CSS_SELECTOR, "option[value='price,desc']")
    SORT_COMPLETE_MESSAGE = (By.CSS_SELECTOR, "div[data-test='sorting_completed']")

    # Search
    SEARCH_QUERY_INPUT = (By.CSS_SELECTOR, "input[data-test='search-query']")
    SEARCH_RESET_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-reset']")
    SEARCH_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    SEARCH_COMPLETE_MESSAGE = (By.CSS_SELECTOR, "div[data-test='search_completed']")

    # Dynamic locator for categories
    CATEGORY_LINK_BY_TEXT = lambda category: (By.LINK_TEXT, category)

    # Items list
    PRODUCT_CARD = (By.CSS_SELECTOR, "a[data-test^='product-']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h5[data-test='product-name']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span[data-test='product-price']")

class LoginPageLocators:
    GOOGLE_SIGNIN_BUTTON = (By.CSS_SELECTOR, "button.google-sign-in-button")
    LOGIN_FORM = (By.CSS_SELECTOR, "form[data-test='login-form']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-test='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-test='password']")
    SHOW_PASSWORD_BUTTON = (By.CLASS_NAME, "btn btn-outline-secondary")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-submit']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[data-test='register-link']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[data-test='forgot-password-link']")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, "div[data-test='login-error']")

class RegisterPageLocators:
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='first-name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='last-name']")
    DOB_INPUT = (By.CSS_SELECTOR, "input[data-test='dob']")
    STREET_INPUT = (By.CSS_SELECTOR, "input[data-test='street']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-test='address']") # used for the with-bugs version instead of street_input
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input[data-test='postal_code']")
    POSTCODE_INPUT = (By.CSS_SELECTOR, "input[data-test='postcode']") # used for the with-bugs version instead of postal_code_input
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-test='city']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-test='state']")
    COUNTRY_SELECT = (By.CSS_SELECTOR, "select[data-test='country']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[data-test='phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-test='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-test='password']")
    SHOW_PASSWORD_BUTTON = (By.CLASS_NAME, "btn btn-outline-secondary")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-test='register-submit']")
    REGISTER_ERROR_MESSAGE = (By.CLASS_NAME, "alert alert-danger")

class ProductDetailsPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1[data-test='product-name']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "span[data-test='unit-price']")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "p[data-test='product-description']")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[data-test='quantity']")
    QUANTITY_DECREASE_BUTTON = (By.CSS_SELECTOR, "button[data-test='decrease-quantity']")
    QUANTITY_INCREASE_BUTTON = (By.CSS_SELECTOR, "button[data-test='increase-quantity']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart']")
    ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-favorites']")

    # Related products
    PRODUCT_CARD = (By.CSS_SELECTOR, "a.card")
    PRODUCT_NAME = (By.CSS_SELECTOR, "h5.card-title")

class ShoppingCartPageLocators:
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(), 'Your shopping cart is empty.')]")
    QUALITY_UPDATED_MESSAGE = (By.CSS_SELECTOR, "div[aria-label='Product quantity updated.']")
    REMOVE_UPDATED_MESSAGE = (By.CSS_SELECTOR, "div[aria-label='Product deleted.']")

    # Step 1 cart
    ITEM_NAME = (By.CSS_SELECTOR, "span[data-test='product-title']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "input[data-test='product-quantity']")
    ITEM_PRICE = (By.CSS_SELECTOR, "span[data-test='product-price']")
    ITEM_TOTAL = (By.CSS_SELECTOR, "span[data-test='line-price']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-danger']")
    CART_TOTAL = (By.CSS_SELECTOR, "td[data-test='cart-total']")
    CHECKOUT_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-1']")

    # Step 2 sign in
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-test='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-test='password']")
    SHOW_PASSWORD_BUTTON = (By.CLASS_NAME, "btn btn-outline-secondary")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-submit']")
    REGISTER_LINK = (By.CSS_SELECTOR, "a[data-test='register-link']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[data-test='forgot-password-link']")
    CHECKOUT_SIGNIN_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-2']")

    # Step 3 address
    STREET_INPUT = (By.CSS_SELECTOR, "input[data-test='street']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[data-test='address']") # used for the with-bugs version instead of street_input
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-test='city']")
    STATE_INPUT = (By.CSS_SELECTOR, "input[data-test='state']")
    COUNTRY_INPUT = (By.CSS_SELECTOR, "input[data-test='country']")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "input[data-test='postal_code']")
    POSTCODE_INPUT = (By.CSS_SELECTOR, "input[data-test='postcode']") # used for the with-bugs version instead of postal_code_input
    CHECKOUT_ADDRESS_BUTTON = (By.CSS_SELECTOR, "button[data-test='proceed-3']")

    # Step 4 payment
    PAYMENT_METHOD_SELECT = (By.CSS_SELECTOR, "select[data-test='payment-method']")
    ACCOUNT_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='account-name']")
    ACCOUNT_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-test='account-number']")
    CONFIRM_BUTTON = (By.CSS_SELECTOR, "button[data-test='finish']")
    # only on normal version
    BANK_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='bank-name']") # bank transfer method, used with account_name_input and account_number_input
    CREDIT_CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-test='credit-card-number']") # credit card method
    EXPIRATION_DATE_INPUT = (By.CSS_SELECTOR, "input[data-test='expiration-date']") # credit card method
    CVV_INPUT = (By.CSS_SELECTOR, "input[data-test='cvv']") # credit card method
    CARD_HOLDER_NAME_INPUT = (By.CSS_SELECTOR, "input[data-test='card-holder-name']") # credit card method
    MONTHLY_INSTALLMENTS_SELECT = (By.CSS_SELECTOR, "select[data-test='monthly-installments']") # buy now pay later method
    GIFT_CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "input[data-test='gift-card-number']") # gift card method
    VALIDATION_CODE_INPUT = (By.CSS_SELECTOR, "input[data-test='validation-code']") # gift card method
    PAYMENT_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[data-test='payment-success-message']")

