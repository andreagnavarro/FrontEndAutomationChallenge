"""
Class that contains all of the test cases to be run.
It also contains code needed to run at the beginning of the tests in order to add the repo's location to path
"""
import sys
import inspect
import os

# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

import argparse
import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjects.OverviewPage import OverviewPage
from PageObjects.ShoppingCartPage import ShoppingCartPage
from PageObjects.CheckoutPage import CheckoutPage
from Tests.BaseTest import BaseTest
from PageObjects.LoginPage import LoginPage
from PageObjects.ProductsPage import ProductsPage
from Resources.TestData import TestData
from Resources.Locators import Locators
from ddt import ddt, data


@ddt
class Tests(BaseTest):

    def setUp(self):
        """
        Setting up website driver
        :param driver: depends on the desired browser
        """
        self.browser = args.browser
        if self.browser == 'chrome':
            self.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        elif self.browser == 'internet_explorer':
            self.driver = webdriver.Ie(TestData.IE_EXECUTABLE_PATH)

    @data("standard_user", "problem_user", "performance_glitch_user")
    def test_login_with_a_valid_user(self, user):
        """
        Test that performs the login sequence with a valid username.
        Validates that the product page gets loaded.
        """
        self.login_page = LoginPage(driver=self.driver, url=TestData.LOGIN_PAGE_URL)
        self.login_page.get_login_page()
        self.login_page.login_sequence(username=user, password=TestData.VALID_PASSWORD)
        self.assertIn(TestData.PRODUCTS_PAGE_KEY_WORD, self.driver.current_url)

    def test_login_with_an_invalid_user(self):
        """
        Test that performs the login sequence with a locked out username.
        Validates that the error message appears on screen.
        """
        self.login_page = LoginPage(driver=self.driver, url=TestData.LOGIN_PAGE_URL)
        self.login_page.get_login_page()
        self.login_page.login_sequence(username=TestData.LOCKED_OUT_USER_NAME, password=TestData.VALID_PASSWORD)
        self.assertTrue(self.login_page.find_element(element_locator=Locators.ERROR_BUTTON))

    def test_logout_from_products_page(self):
        """
        Test that perform the logout sequence from the product's page.
        Validates that the login page loads.
        """
        self.products_page = ProductsPage(driver=self.driver, url=TestData.PRODUCTS_PAGE_URL)
        self.products_page.get_products_page()
        self.products_page.logout_sequence()
        self.assertTrue(self.products_page.find_element(element_locator=Locators.LOGIN_BUTTON))

    def test_navigate_to_the_shopping_cart(self):
        """
        Test that navigates to the product page and click on the shopping cart
        Validates that the shopping cart page loads
        """
        self.products_page = ProductsPage(driver=self.driver, url=TestData.PRODUCTS_PAGE_URL)
        self.products_page.get_products_page()
        self.products_page.click_on_shopping_cart()
        self.assertIn(TestData.CART_PAGE_URL_PARTIAL, self.driver.current_url)

    def test_add_single_item_to_cart(self):
        """
        Test that navigates to the products page, adds an item to the cart and make sure the item is in the cart
        Validates that the item selected was correctly added to the cart
        """
        self.products_page = ProductsPage(driver=self.driver, url=TestData.PRODUCTS_PAGE_URL)
        self.products_page.get_products_page()
        self.products_page.click_add_first_item_to_cart_button()
        self.products_page.click_on_shopping_cart()
        self.assertTrue(self.products_page.find_element(element_locator=Locators.SAUCE_LABS_BACKPACK))

    def test_add_multiple_items_to_cart(self):
        """
        Test that navigates to the products page, adds the first two items to the cart
        Validates that both items selected were correctly added to the cart
        """
        self.products_page = ProductsPage(driver=self.driver, url=TestData.PRODUCTS_PAGE_URL)
        self.products_page.get_products_page()
        self.products_page.click_add_first_item_to_cart_button()
        self.products_page.click_add_second_item_to_cart_button()
        self.products_page.click_on_shopping_cart()
        self.assertTrue(self.products_page.find_element(element_locator=Locators.SAUCE_LABS_BACKPACK) and
                        self.products_page.find_element(element_locator=Locators.SAUCE_LABS_BIKE_LIGHT))

    def test_continue_with_missing_mail_information(self):
        """
        Test that navigates to the checkout page and clicks continue without any of the users information
        Validates that the missing information error is displayed
        """
        self.checkout_page = CheckoutPage(driver=self.driver, url=TestData.CHECKOUT_PAGE_URL)
        self.checkout_page.get_checkout_page()
        self.checkout_page.click_continue_button()
        self.assertTrue(self.checkout_page.find_element(element_locator=Locators.MISSING_INFORMATION_ERROR))

    def test_fill_users_information(self):
        """
        Test that navigates to the checkout page and fills out the users information and clicks on the continue button
        Validates that the overview page loads correctly
        """
        self.checkout_page = CheckoutPage(driver=self.driver, url=TestData.CHECKOUT_PAGE_URL)
        self.checkout_page.get_checkout_page()
        self.checkout_page.fill_out_users_information()
        self.checkout_page.click_continue_button()
        self.assertIn(TestData.CHECKOUT_PAGE_STEP_TWO_PARTIAL_URL, self.driver.current_url)

    def test_final_order_items(self):
        """
        Test that navigates to the products page and adds one item, then navigates to the checkout page, fills out the
        users information and verifies the product was the correct one
        Validates that the item in the overview page matches with the added item
        """
        self.products_page = ProductsPage(driver=self.driver, url=TestData.PRODUCTS_PAGE_URL)
        self.products_page.get_products_page()
        self.products_page.click_add_first_item_to_cart_button()
        self.products_page.click_add_second_item_to_cart_button()
        self.products_page.click_on_shopping_cart()
        self.shopping_cart_page = ShoppingCartPage(driver=self.driver, url=TestData.CART_PAGE_URL)
        self.shopping_cart_page.click_on_checkout_button()
        self.checkout_page = CheckoutPage(driver=self.driver, url=TestData.CHECKOUT_PAGE_URL)
        self.checkout_page.fill_out_users_information()
        self.checkout_page.click_continue_button()
        self.assertTrue(self.products_page.find_element(element_locator=Locators.SAUCE_LABS_BACKPACK) and
                        self.products_page.find_element(element_locator=Locators.SAUCE_LABS_BIKE_LIGHT))

    def test_complete_a_purchase(self):
        """
        Test that navigates to the overview page and clicks the finish button
        Validates that the confirmation page is loaded correctly
        """
        self.overview_page = OverviewPage(driver=self.driver, url=TestData.OVERVIEW_PAGE_URL)
        self.overview_page.get_overview_page()
        self.overview_page.click_on_finish_button()
        self.assertIn(TestData.CONFIRMATION_PAGE_PARTIAL_URL, self.driver.current_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', help='Desired browser', dest='browser')
    parser.add_argument('unittest_args', nargs='*')
    args = parser.parse_args()
    sys.argv[1:] = args.unittest_args
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.REPORTS))
