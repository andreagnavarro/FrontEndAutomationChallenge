"""
Class that includes the setup and tearDown functions that will execute before and after each test, respectively.
"""
import unittest

from selenium import webdriver

from FrontEndAutomationChallenge.Resources.TestData import TestData


class BaseTest(unittest.TestCase):

    def setUp(self):
        """
        Setting up website driver
        :param driver: depends on the desired browser
        """
        self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)

    def tearDown(self):
        """
        Cleanup after test has executed
        :return:
        """
        self.driver.close()
        self.driver.quit()
