"""
Class for the actions that can be done in the checkout page. These include getting the actual webpage and filling out
the users information needed for checkout
"""
from FrontEndAutomationChallenge.PageObjects.BasePage import BasePage
from FrontEndAutomationChallenge.Resources.Locators import Locators
from FrontEndAutomationChallenge.Resources.TestData import TestData


class CheckoutPage(BasePage):
    def __init__(self, driver, url):
        """
        Constructor that initializes url and driver attributes and instantiates a BasePase object
        :param driver: browser's driver
        :param url: checkout website's url
        """
        super().__init__(driver)
        self.url = url
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_checkout_page(self):
        """
        Gets checkout page
        """
        self.base_page.get_page(url=self.url)

    def click_continue_button(self):
        """
        Clicks on the continue button of the checkout page
        """
        self.base_page.click_on_element(element_locator=Locators.CONTINUE_BUTTON)

    def fill_out_users_information(self):
        """
        Fills out First Name, LastName and ZIP info on the checkout page
        """
        first_name_box = self.base_page.find_element(element_locator=Locators.FIRST_NAME_BOX)
        first_name_box.clear()
        self.base_page.write_to_element(element_locator=Locators.FIRST_NAME_BOX, text=TestData.FIRST_NAME)
        last_name_box = self.base_page.find_element(element_locator=Locators.LAST_NAME_BOX)
        last_name_box.clear()
        self.base_page.write_to_element(element_locator=Locators.LAST_NAME_BOX, text=TestData.LAST_NAME)
        postal_code_box = self.base_page.find_element(element_locator=Locators.POSTAL_CODE_BOX)
        postal_code_box.clear()
        self.base_page.write_to_element(element_locator=Locators.POSTAL_CODE_BOX, text=TestData.POSTAL_CODE)
