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
    ADD_TO_CART_BUTTON_1 = (By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button")
    ADD_TO_CART_BUTTON_2 = (By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/button")
    # Shopping cart Page locators
    SAUCE_LABS_BACKPACK = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    SAUCE_LABS_BIKE_LIGHT = (By.XPATH, "//div[text()='Sauce Labs Bike Light']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[text()='CHECKOUT']")
    # Checkout Page locators
    CONTINUE_BUTTON = (By.XPATH, "//*[@id='checkout_info_container']/div/form/div[2]/input")
    FIRST_NAME_BOX = (By.ID, "first-name")
    LAST_NAME_BOX = (By.ID, "last-name")
    POSTAL_CODE_BOX = (By.ID, "postal-code")
    MISSING_INFORMATION_ERROR = (By.XPATH, "//*[@id='checkout_info_container']/div/form/h3")
    # Overview Page locators
    FINISH_BUTTON = (By.XPATH, "//a[text()='FINISH']")

