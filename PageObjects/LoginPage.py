"""
Class for the actions that can be done in the Login page. These include getting the actual webpage and executing the
login sequence
"""
from FrontEndAutomationChallenge.PageObjects.BasePage import BasePage
from FrontEndAutomationChallenge.Resources.Locators import Locators


class LoginPage(BasePage):
    def __init__(self, driver, url):
        """
        Constructor that initializes url and driver attributes and instantiates a BasePase object
        :param driver: browser's driver
        :param url: login website's url
        """
        super().__init__(driver)
        self.url = url
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_login_page(self):
        """
        Gets the login page
        """
        self.base_page.get_page(url=self.url)

    def login_sequence(self, username, password):
        """
        Performs the login sequence which includes the following steps:
        1. Get the username box
        2. Clear the username box
        3. Enter the given username
        4. Get the password box
        5. Clear the password box
        6. Enter the given password
        7. Click on the login button
        :return:
        """
        username_box = self.base_page.find_element(Locators.USERNAME_BOX)
        username_box.clear()
        self.base_page.write_to_element(element_locator=Locators.USERNAME_BOX, text=username)
        password_box = self.base_page.find_element(Locators.PASSWORD_BOX)
        password_box.clear()
        self.base_page.write_to_element(element_locator=Locators.PASSWORD_BOX, text=password)
        self.base_page.click_on_element(Locators.LOGIN_BUTTON)
