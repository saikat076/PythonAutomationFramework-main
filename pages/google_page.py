from selenium.webdriver.common.by import By
from locators.google_locators import GoogleLocators

class GooglePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_google(self):
        self.drive.maximize_window()
        self.driver.get("https://www.google.com/")

    def search(self, term):
        search_box = self.driver.find_element(*GoogleLocators.SEARCH_BOX)