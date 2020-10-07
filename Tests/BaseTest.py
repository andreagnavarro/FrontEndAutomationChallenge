"""
Class that includes the setup and tearDown functions that will execute before and after each test, respectively.
"""
import unittest
from selenium import webdriver
from Resources.TestData import TestData


class BaseTest(unittest.TestCase):



    def tearDown(self):
        """
        Cleanup after test has executed
        :return:
        """
        self.driver.close()
        self.driver.quit()
