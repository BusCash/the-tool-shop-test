# pages/homepage.py
from pages.base_page import BasePage
from pages.utils.locators import HomePageLocators, CommonLocators
from pages.utils.config import BASE_URL

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    def load(self):
        self.go_to_url(self.url)

    def select_sort_default_option(self):
        self.click(HomePageLocators.SORT_OPTION)
        self.wait_for_element(HomePageLocators.SORT_COMPLETE_MESSAGE)

    def select_sort_name_asc_option(self):
        self.click(HomePageLocators.SORT_NAME_ASC_OPTION)
        self.wait_for_element(HomePageLocators.SORT_COMPLETE_MESSAGE)

    def select_sort_name_desc_option(self):
        self.click(HomePageLocators.SORT_NAME_DESC_OPTION)
        self.wait_for_element(HomePageLocators.SORT_COMPLETE_MESSAGE)

    def select_sort_price_asc_option(self):
        self.click(HomePageLocators.SORT_PRICE_ASC_OPTION)
        self.wait_for_element(HomePageLocators.SORT_COMPLETE_MESSAGE)

    def select_sort_price_desc_option(self):
        self.click(HomePageLocators.SORT_PRICE_DESC_OPTION)
        self.wait_for_element(HomePageLocators.SORT_COMPLETE_MESSAGE)

    def search(self, query):
        self.type_text(HomePageLocators.SEARCH_QUERY_INPUT, query)
        self.click(HomePageLocators.SEARCH_SUBMIT_BUTTON)
        self.wait_for_element(HomePageLocators.SEARCH_COMPLETE_MESSAGE)

    def reset_search(self):
        self.click(HomePageLocators.SEARCH_RESET_BUTTON)
        self.wait_for_element(HomePageLocators.SEARCH_COMPLETE_MESSAGE)

    def click_product(self, name):
        self.click(next(p for p in self.find_elements(HomePageLocators.PRODUCT_NAME) if p.text == name))

    def ctrl_click_product(self, name):
        self.ctrl_click(next(p for p in self.find_elements(HomePageLocators.PRODUCT_NAME) if p.text == name))

    def click_product_by_index(self, idx):
        self.click([p for p in self.find_elements(HomePageLocators.PRODUCT_NAME)][idx])

    def ctrl_click_product_by_index(self, idx):
        self.ctrl_click([p for p in self.find_elements(HomePageLocators.PRODUCT_NAME)][idx])

    def click_category(self, category_name): #Not fixed yet
        self.click(HomePageLocators.CATEGORY_LINK_BY_TEXT(category_name))
