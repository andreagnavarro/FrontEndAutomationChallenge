"""
Class for the actions that can be done in the checkout page. These include getting the actual webpage and filling out
the users information needed for checkout
"""
from PageObjects.BasePage import BasePage
from Resources.Locators import Locators


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

    def fill_out_users_first_name(self, first_name):
        """
        Clears out the box for the users first name, then writes the text given
        :param first_name: Text that will be the input for the first name box
        """
        first_name_box = self.base_page.find_element(element_locator=Locators.FIRST_NAME_BOX)
        first_name_box.clear()
        self.base_page.write_to_element(element_locator=Locators.FIRST_NAME_BOX, text=first_name)

    def fill_out_users_last_name(self, last_name):
        """
        Clears out the box for the users last name, then writes the text given
        :param last_name: Text that will be the input for the last name box
        """
        last_name_box = self.base_page.find_element(element_locator=Locators.LAST_NAME_BOX)
        last_name_box.clear()
        self.base_page.write_to_element(element_locator=Locators.LAST_NAME_BOX, text=last_name)

    def fill_out_users_postal_code_name(self, postal_code):
        """
        Clears out the box for the users postal code, then writes the text given
        :param postal_code: Text that will be the input for the postal code box
        """
        postal_code_box = self.base_page.find_element(element_locator=Locators.POSTAL_CODE_BOX)
        postal_code_box.clear()
        self.base_page.write_to_element(element_locator=Locators.POSTAL_CODE_BOX, text=postal_code)

    def is_missing_info_error_visible(self):
        """
        Function that verifies that the missing information error appears on screen
        :return: True if the error is present, false otherwise
        """
        if self.base_page.find_element(element_locator=Locators.MISSING_INFORMATION_ERROR):
            return True
        else:
            return False
