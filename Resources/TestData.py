"""
Class that includes test data constants
"""
import os


class TestData:
    CHROME_EXECUTABLE_PATH = os.path.join(os.path.abspath("."), "Drivers", "chromedriver.exe")
    IE_EXECUTABLE_PATH = os.path.join(os.path.abspath("."), "Drivers", "IEDriverServer.exe")
    REPORTS = os.path.join(os.path.abspath("."), "Reports")
    STANDARD_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    PRODUCTS_PAGE_KEY_WORD = "inventory"
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    LOCKED_OUT_USER_NAME = "locked_out_user"
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CART_PAGE_URL_PARTIAL = "cart"
    FIRST_NAME = "Andrea"
    LAST_NAME = "Navarro"
    POSTAL_CODE = "45010"
    CHECKOUT_PAGE_STEP_TWO_PARTIAL_URL = "checkout-step-two"
    OVERVIEW_PAGE_URL = "https://www.saucedemo.com/checkout-step-two.html"
    CONFIRMATION_PAGE_PARTIAL_URL = "checkout-complete"


