"""
Class for the actions that can be done in the Overview page. These include getting the actual webpage and clicking
on the finish order button
"""
from PageObjects.BasePage import BasePage
from Resources.Locators import Locators


class OverviewPage(BasePage):
    def __init__(self, driver, url):
        """
        Constructor that initializes url and driver attributes
        :param driver: browser's driver
        :param url: Overview website's url
        """
        super().__init__(driver)
        self.url = url
        self.driver = driver
        self.base_page = BasePage(self.driver)

    def get_overview_page(self):
        """
        Gets overview website
        """
        self.base_page.get_page(url=self.url)

    def click_on_finish_button(self):
        """
        Clicks on the finish button on the overview page
        """
        self.click_on_element(element_locator=Locators.FINISH_BUTTON)
