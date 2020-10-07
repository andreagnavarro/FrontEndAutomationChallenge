"""
Class that includes the tearDown function that will execute after each test.
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
