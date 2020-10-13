"""
Class for the actions that can be done in the Products page. These include getting the actual webpage and executing the
logout sequence as well as handling the items
"""
from PageObjects.BasePage import BasePage
from Resources.Locators import Locators


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

    def click_add_item_to_cart_button(self, positions):
        """
        Clicks on the first item's add to cart button on the products page
        This first item is the Sauce Labs Backpack
        :param positions: list of the position of the item to be added to cart
        """
        for position in positions:
            item = Locators.get_item_locator_products_page(position=position)
            self.base_page.click_on_element(element_locator=item)

    def is_login_button_visible(self):
        """
        Function that asserts the visibility of the login button
        :return: True if the login button is found on the page, false otherwise
        """

        if self.base_page.find_element(element_locator=Locators.LOGIN_BUTTON):
            return True
        else:
            return False

    def is_item_visible(self, positions):
        """
        Function that verifies that every single item added to the cart is visible in the cart.
        This is done by receiving a list of positions and verifying that the amount of positions is the same amount of
        items
        :param positions: list of the positions of the items to verify
        :return: True if the amount of positions and the amount of items in the cart match
        """
        i = 1
        for position in positions:
            item = Locators.get_item_locator_checkout_page(position=i)
            if not self.base_page.find_element(element_locator=item):
                return False
            i += 1
        return True

