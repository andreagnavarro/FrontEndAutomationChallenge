"""
Class that includes functions with basic actions within a webpage.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        """
        Class constructor, sets the driver for the browser
        :param driver: Browser's driver
        """
        self.driver = driver

    def get_page(self, url):
        """
        Gets a webpage corresponding to the given URL with the given browser
        """
        self.driver.get(url)

    def write_to_element(self, element_locator, text):
        """
        Waits a maximum of 10 seconds to find the given element then sends the given smell to the element
        :param element_locator: the element's reference
        :param text: String of text to write on the given element
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator)).send_keys(text)

    def click_on_element(self, element_locator):
        """
        Waits a maximum of 10 seconds to find the given element then clicks on it
        :param element_locator: the element's reference
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator)).click()

    def find_element(self, element_locator):
        """
        Waits a maximum of 10 seconds to find an element by its reference
        :param element_locator: the element's reference
        :return: element
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_locator))