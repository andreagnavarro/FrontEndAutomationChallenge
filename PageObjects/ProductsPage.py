"""
Class for the actions that can be done in the Products page. These include getting the actual webpage and executing the
logout sequence as well as handling the items
"""
from FrontEndAutomationChallenge.PageObjects.BasePage import BasePage
from FrontEndAutomationChallenge.Resources.Locators import Locators


class ProductsPage(BasePage):
    def __init__(self, driver, url):
        """
        Constructor that initializes url and driver attributes
        :param driver: browser's driver
        :param url: products website's url
        """
        super().__init__(driver)
        self.url = url
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_products_page(self):
        """
        Gets products website
        """
        self.base_page.get_page(url=self.url)

    def logout_sequence(self):
        """
        Performs the logout sequence from the products page
        """
        self.base_page.click_on_element(element_locator=Locators.SIDEBAR_BUTTON)
        self.base_page.click_on_element(element_locator=Locators.LOGOUT_BUTTON)

    def click_on_shopping_cart(self):
        """
        Clicks on shopping cart button that takes the user to shopping cart page
        """
        self.base_page.click_on_element(element_locator=Locators.SHOPPING_CART)

    def click_add_first_item_to_cart_button(self):
        """
        Clicks on the first item's add to cart button on the products page
        This first item is the Sauce Labs Backpack
        """
        self.base_page.click_on_element(element_locator=Locators.ADD_TO_CART_BUTTON_1)

    def click_add_second_item_to_cart_button(self):
        """
        Clicks on the second item's add to cart button on the products page
        This second item is the Sauce Labs Bike Light
        """
        self.base_page.click_on_element(element_locator=Locators.ADD_TO_CART_BUTTON_2)
