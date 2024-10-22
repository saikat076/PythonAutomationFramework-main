from selenium.webdriver.common.by import By

class GoogleLocators:
    SEARCH_BOX = (By.XPATH, "//textarea[@name='q']")
    TARGET_ELEMENT = (By.XPATH, "//*[@id='rso']/div[6]/div/div/div[1]/div/div/span/a/h3")
    FLIPKART_SEARCH_BAR = (By.XPATH, "//input[@class='Pke_EE']")
    FIRST_MOBILE = (By.XPATH, "(//div[@class='KzDlHZ'])[1]")
    MOBILE_NAME = (By.XPATH, "//span[@class='VU-ZEz']")
    HOMEPAGE_LOGO = (By.XPATH, "//a/img[@alt='Website for automation practice']")
    SIGN_UP_OR_LOG_IN_LINK = (By.XPATH, "//a[@href='/login']")
    NAME_TEXTBOX = (By.XPATH, "//input[@data-qa='signup-name']")
    EMAIL_TEXTBOX = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGN_UP_BTN = (By.XPATH, "//button[@data-qa='signup-button']")