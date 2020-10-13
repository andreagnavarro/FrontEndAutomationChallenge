"""
Class with element locators separated by page
"""
from selenium.webdriver.common.by import By


class Locators:
    # Login Page locators
    USERNAME_BOX = (By.ID, "user-name")
    PASSWORD_BOX = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn_action")
    ERROR_BUTTON = (By.XPATH, "//*[@id='login_button_container']/div/form/h3/button")
    # Products Page locators
    SIDEBAR_BUTTON = (By.CLASS_NAME, "bm-burger-button")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    SHOPPING_CART = (By.ID, "shopping_cart_container")
    # Shopping cart Page locators
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='CHECKOUT']")
    # Checkout Page locators
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input")
    FIRST_NAME_BOX = (By.ID, "first-name")
    LAST_NAME_BOX = (By.ID, "last-name")
    POSTAL_CODE_BOX = (By.ID, "postal-code")
    MISSING_INFORMATION_ERROR = (By.XPATH, "//*[@id='checkout_info_container']/div/form/h3")
    # Overview Page locators
    FINISH_BUTTON = (By.XPATH, "//a[text()='FINISH']")

    @staticmethod
    def get_item_locator_products_page(position):
        """
        Function that determines the locator of an "add to cart" button of an item based on its position.
        Example, if the parameter position = "1" the first item displayed will be the one returned.
        :param position: the position of the item to obtain the locator
        :return: the locator of the "add to cart" button of the requested item
        """
        return By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[{}]/div[3]/button".format(position)

    @staticmethod
    def get_item_locator_checkout_page(position):
        """
        Function that determines the locator of item in the cart. The xpath is shifted by 2, so in order to get the
        correct locator, first the shift has to be implemented.
        :param position: the position of the item to obtain the locator
        :return: the locator of the requested item in the cart
        """
        position += 2
        return By.XPATH, "/html/body/div/div[2]/div[3]/div/div[1]/div[{}]".format(str(position))
