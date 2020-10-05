from FrontEndAutomationChallenge.PageObjects.OverviewPage import OverviewPage
from FrontEndAutomationChallenge.PageObjects.ShoppingCartPage import ShoppingCartPage
from FrontEndAutomationChallenge.PageObjects.CheckoutPage import CheckoutPage
from FrontEndAutomationChallenge.Tests.BaseTest import BaseTest
from FrontEndAutomationChallenge.PageObjects.LoginPage import LoginPage
from FrontEndAutomationChallenge.PageObjects.ProductsPage import ProductsPage
from FrontEndAutomationChallenge.Resources.TestData import TestData
from FrontEndAutomationChallenge.Resources.Locators import Locators


class Tests(BaseTest):

    def test_login_with_a_valid_user(self):
        """
        Test that performs the login sequence with a valid username.
        Validates that the product page gets loaded.
        """
        self.login_page = LoginPage(driver=self.driver, url=TestData.LOGIN_PAGE_URL)
        self.login_page.get_login_page()
        self.login_page.login_sequence(username=TestData.STANDARD_USERNAME, password=TestData.VALID_PASSWORD)
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
