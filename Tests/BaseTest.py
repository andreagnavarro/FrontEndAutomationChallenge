"""
Class that includes the tearDown function that will execute after each test.
"""
import unittest


class BaseTest(unittest.TestCase):

    def tearDown(self):
        """
        Cleanup after test has executed
        :return:
        """
        self.driver.close()
        self.driver.quit()
