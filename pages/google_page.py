from selenium.webdriver.common.by import By
from locators.google_locators import GoogleLocators
from utils.screenshot import take_screenshot
import time

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_google(self):
        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")

    def search(self, term):

        search_box = self.driver.find_element(*GoogleLocators.SEARCH_BOX)
        search_box.send_keys(term)
        take_screenshot(self.driver, "Test")
        search_box.submit()

    def get_target_element(self):
        return self.driver.find_element(*GoogleLocators.TARGET_ELEMENT)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def navigate_to_flipkart(self):
        self.driver.maximize_window()
        self.driver.get("https://www.flipkart.com")
    
    def search_for(self, search_term):
        flipkart_search_box = self.driver.find_element(*GoogleLocators.FLIPKART_SEARCH_BAR)
        flipkart_search_box.send_keys(search_term)
        take_screenshot(self.driver, "Searching_For_Mobile")
        flipkart_search_box.submit()

    def choose_first_mobile(self):
        take_screenshot(self.driver, "Search_Result_Page")
        first_mobile = self.driver.find_element(*GoogleLocators.FIRST_MOBILE)
        first_mobile.click()

    def validate_mobile_name(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        take_screenshot(self.driver, "Mobile_Details_Page")

        mobile_name = self.driver.find_element(*GoogleLocators.MOBILE_NAME)

        if "OPPO" in mobile_name.text:
            print("Validation successful")
        else:
            print("Validation failed")
            AssertionError()

    def open_exercise_homepage_and_validate(self):
        self.driver.maximize_window()
        self.driver.get("https://automationexercise.com/")

        homepage_logo = self.driver.find_element(*GoogleLocators.HOMEPAGE_LOGO)

        take_screenshot(self.driver, "Validate Homepage")
        if not homepage_logo.is_displayed():
            AssertionError()

    def fill_details_and_sign_up(self):
        sign_up_or_log_in = self.driver.find_element(*GoogleLocators.SIGN_UP_OR_LOG_IN_LINK)
        sign_up_or_log_in.click()
        
        time.sleep(3)
        take_screenshot(self.driver, "Sign up Page")

        name_textbox = self.driver.find_element(*GoogleLocators.NAME_TEXTBOX)
        email_textbox = self.driver.find_element(*GoogleLocators.EMAIL_TEXTBOX)

        name_textbox.send_keys("Saikat")
        email_textbox.send_keys("saikat@gmail.com")

        signup_btn = self.driver.find_element(*GoogleLocators.SIGN_UP_BTN)
        signup_btn.click()

        time.sleep(10)

        take_screenshot(self.driver, "Fill details page")

