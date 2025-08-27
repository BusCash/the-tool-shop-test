# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.utils.config import BASE_URL, EXPLICIT_WAIT_TIME
from pages.utils.locators import CommonLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT_TIME)
        self.base_url = BASE_URL

    def go_to_url(self, url=""):
        """Navigates to the specified URL or base URL if none provided."""
        full_url = f"{url}"
        self.driver.get(full_url)
        self.wait_for_page_load()

    def wait_for_page_load(self):
        """Waits until the document.readyState is 'complete'."""
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    def wait_for_element(self, by_locator):
        """Waits for an element to be present in the DOM."""
        try:
            return self.wait.until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {by_locator} not found after {EXPLICIT_WAIT_TIME} seconds.")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator {by_locator} not found.")

    def find_element(self, by_locator):
        """Waits for an element to be visible and returns it."""
        try:
            return self.wait.until(EC.visibility_of_element_located(by_locator))
        except TimeoutException:
            raise TimeoutException(f"Element with locator {by_locator} not visible after {EXPLICIT_WAIT_TIME} seconds.")
        except NoSuchElementException:
            raise NoSuchElementException(f"Element with locator {by_locator} not found.")

    def find_elements(self, by_locator):
        """Waits for elements to be present and returns a list of them."""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(by_locator))
        except TimeoutException:
            raise TimeoutException(f"No elements with locator {by_locator} present after {EXPLICIT_WAIT_TIME} seconds.")

    def click(self, by_locator):
        """Waits for an element to be clickable and clicks it."""
        try:
            self.wait.until(EC.element_to_be_clickable(by_locator)).click()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {by_locator} not clickable after {EXPLICIT_WAIT_TIME} seconds.")
        
    def ctrl_click(self, by_locator):
        """Waits for an element to be clickable and clicks it."""
        try:
            ActionChains(self.driver).key_down(Keys.CONTROL).click(self.wait.until(EC.element_to_be_clickable(by_locator))).key_up(Keys.CONTROL).perform()
        except TimeoutException:
            raise TimeoutException(f"Element with locator {by_locator} not clickable after {EXPLICIT_WAIT_TIME} seconds.")

    def type_text(self, by_locator, text):
        """Waits for an element to be visible, clears it, and types text."""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        """Waits for an element to be visible and returns its text."""
        return self.find_element(by_locator).text.strip()
    
    def get_price(self, by_locator):
        """Waits for an element to be visible and returns its price as a float."""
        price_text = self.get_text(by_locator)
        try:
            return float(price_text.replace('$', '').replace(',', '').replace('.', ''))
        except ValueError:
            raise ValueError(f"Could not convert price text '{price_text}' to float.")

    def is_element_present(self, by_locator):
        """Checks if an element is present in the DOM."""
        try:
            self.driver.find_element(*by_locator)
            return True
        except NoSuchElementException:
            return False

    def get_success_message(self):
        """Returns the text of the global success message."""
        try:
            return self.find_element(CommonLocators.SUCCESS_MESSAGE).text
        except (TimeoutException, NoSuchElementException):
            return None

    def get_error_message(self):
        """Returns the text of the global error message."""
        try:
            return self.find_element(CommonLocators.ERROR_MESSAGE).text
        except (TimeoutException, NoSuchElementException):
            return None
        
    def get_bug_message(self):
        """Returns the text of the global error message."""
        try:
            return self.find_element(CommonLocators.BUG_MESSAGE).text
        except (TimeoutException, NoSuchElementException):
            return None
        
    def switch_to_tab(self, index):
        """Switches to a specific browser tab by index."""
        try:
            self.driver.switch_to.window(self.driver.window_handles[index])
        except IndexError:
            raise IndexError(f"No tab found at index {index}. Current tabs: {self.driver.window_handles}")
        except Exception as e:
            raise Exception(f"Failed to switch to tab at index {index}: {str(e)}")
        
    def close_tab(self):
        """Closes the current browser tab."""
        try:
            self.driver.close()
            # Switch back to the first tab if available
            if len(self.driver.window_handles) > 0:
                self.driver.switch_to.window(self.driver.window_handles[0])
        except Exception as e:
            raise Exception(f"Failed to close the current tab: {str(e)}")

    # Nav bar behavior methods
    def click_logo(self):
        """Clicks the site logo to navigate to the home page."""
        self.click(CommonLocators.LOGO)

    def click_menu(self):
        """Clicks the main menu button to open the navigation menu."""
        self.click(CommonLocators.MENU)
    
    def click_nav_home(self):
        """Clicks the home navigation link."""
        self.click(CommonLocators.NAV_HOME)

    def click_nav_categories(self):
        """Clicks the categories navigation link."""
        self.click(CommonLocators.NAV_CATEGORIES)

    def click_nav_hand_tools(self):
        """Clicks the hand tools navigation link."""
        self.click(CommonLocators.NAV_HAND_TOOLS)

    def click_nav_power_tools(self):
        """Clicks the power tools navigation link."""
        self.click(CommonLocators.NAV_POWER_TOOLS)

    def click_nav_other(self):
        """Clicks the other tools navigation link."""
        self.click(CommonLocators.NAV_OTHER)

    def click_nav_special_tools(self):
        """Clicks the special tools navigation link."""
        self.click(CommonLocators.NAV_SPECIAL_TOOLS)

    def click_nav_rentals(self):
        """Clicks the rentals navigation link."""
        self.click(CommonLocators.NAV_RENTALS)

    def click_nav_contact(self):
        """Clicks the contact navigation link."""
        self.click(CommonLocators.NAV_CONTACT)

    def click_nav_sign_in(self):
        """Clicks the sign in navigation link."""
        self.click(CommonLocators.NAV_SIGN_IN)

    def click_nav_cart(self):
        """Clicks the cart navigation link."""
        self.click(CommonLocators.NAV_CART)

    def click_nav_language_select(self):
        """Clicks the language select dropdown."""
        self.click(CommonLocators.LANGUAGE_SELECT)

    def select_language(self, language):
        """Selects a language from the dropdown."""
        language_locators = {
            'de': CommonLocators.LANG_DE,
            'en': CommonLocators.LANG_EN,
            'es': CommonLocators.LANG_ES,
            'fr': CommonLocators.LANG_FR,
            'nl': CommonLocators.LANG_NL,
            'tr': CommonLocators.LANG_TR
        }
        if language in language_locators:
            self.click(language_locators[language])
        else:
            raise ValueError(f"Language '{language}' not supported.")
        
    def click_nav_menu(self):
        """Clicks the navigation menu link."""
        self.click(CommonLocators.NAV_MENU)

    def click_nav_my_account(self):
        """Clicks the my account navigation link."""
        self.click(CommonLocators.NAV_MY_ACCOUNT)

    def click_nav_my_favorites(self):
        """Clicks the my favorites navigation link."""
        self.click(CommonLocators.NAV_MY_FAVORITES)

    def click_nav_my_profile(self):
        """Clicks the my profile navigation link."""
        self.click(CommonLocators.NAV_MY_PROFILE)

    def click_nav_my_invoices(self):
        """Clicks the my invoices navigation link."""
        self.click(CommonLocators.NAV_MY_INVOICES)

    def click_nav_my_messages(self):
        """Clicks the my messages navigation link."""
        self.click(CommonLocators.NAV_MY_MESSAGES)

    def click_nav_sign_out(self):
        """Clicks the sign out navigation link."""
        self.click(CommonLocators.NAV_SIGN_OUT)

    def get_cart_item_count(self):
        """Returns the number of items in the cart."""
        try:
            return self.get_text(CommonLocators.NAV_CART_QUANTITY)
        except (TimeoutException, NoSuchElementException, IndexError, ValueError):
            return 0