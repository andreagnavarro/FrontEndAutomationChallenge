"""
Class for the actions that can be done in the Shopping Cart page. These include getting the actual webpage and clicking
on the checkout button
"""
from FrontEndAutomationChallenge.PageObjects.BasePage import BasePage
from FrontEndAutomationChallenge.Resources.Locators import Locators


class ShoppingCartPage(BasePage):
    def __init__(self, driver, url):
        """
        Constructor that initializes url and driver attributes
        :param driver: browser's driver
        :param url: shopping cart website's url
        """
        super().__init__(driver)
        self.url = url
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_shopping_cart_page(self):
        """
        Gets shopping cart website
        """
        self.base_page.get_page(url=self.url)

    def click_on_checkout_button(self):
        """
        Clicks on the checkout button on the cart page
        """
        self.click_on_element(element_locator=Locators.CHECKOUT_BUTTON)
