from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.google_page import GooglePage
#from utils.screenshot import take_screenshot
import time

@given('I open Google homepage')
def step_open_google_homepage(context):
    chrome_driver_path = '/Users/saikatbhattacharyya/Downloads/chromedriver-mac-x64 3/chromedriver'
    service = Service(executable_path=chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.google_page = GooglePage(context.driver)
    context.google_page.navigate_to_google()

@when('I search for "{search_term}"')
def step_search_google(context, search_term):
    context.google_page.search(search_term)