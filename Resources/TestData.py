"""
Class that includes test data constants
"""
import os


class TestData:
    # Drivers executable paths
    CHROME_EXECUTABLE_PATH = os.path.join(os.path.abspath("."), "Drivers", "chromedriver.exe")
    IE_EXECUTABLE_PATH = os.path.join(os.path.abspath("."), "Drivers", "IEDriverServer.exe")

    # Pages URL
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    OVERVIEW_PAGE_URL = "https://www.saucedemo.com/checkout-step-two.html"

    # Partial URLS
    CHECKOUT_PAGE_STEP_TWO_PARTIAL_URL = "checkout-step-two"
    CONFIRMATION_PAGE_PARTIAL_URL = "checkout-complete"
    CART_PAGE_URL_PARTIAL = "cart"
    PRODUCTS_PAGE_KEY_WORD = "inventory"

    # Directories
    REPORTS = os.path.join(os.path.abspath("."), "Reports")

    # User data
    STANDARD_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    LOCKED_OUT_USER_NAME = "locked_out_user"
    FIRST_NAME = "Andrea"
    LAST_NAME = "Navarro"
    POSTAL_CODE = "45010"

    # Constants
    FIST_POSITION = ["1"]


