from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pages.google_page import GooglePage
from utils.screenshot import take_screenshot
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

@then('I scroll to the target search result element')
def step_scroll_to_target_element(context):
    target_element = context.google_page.get_target_element()
    context.google_page.scroll_to_element(target_element)
    time.sleep(2)

@given('I open flipkart homepage')
def I_open_flipkart_homepage(context):
    chrome_driver_path = '/Users/saikatbhattacharyya/Downloads/chromedriver-mac-x64 3/chromedriver'
    service = Service(executable_path=chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.google_page = GooglePage(context.driver)
    context.google_page.navigate_to_flipkart()

@when('I search in flipkart for "{search_term}"')
def I_search_in_flipkart_for_mobile(context, search_term):
    context.google_page.search_for(search_term)

@then(u'I choose the first mobile available')
def I_choose_the_first_mobile_available(context):
    context.google_page.choose_first_mobile()

@then(u'I validate the mobile name')
def I_validate_the_mobile_name(context):
    context.google_page.validate_mobile_name()

@given('I open automation exercise homepage and validate')
def I_open_automation_exercise_homepage_and_validate(context):
    chrome_driver_path = '/Users/saikatbhattacharyya/Downloads/chromedriver-mac-x64 3/chromedriver'
    service = Service(executable_path=chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.google_page = GooglePage(context.driver)
    context.google_page.open_exercise_homepage_and_validate()

@then('I go to signup page to fill details and click on signup button')
def I_go_to_signup_page_to_fill_details_and_click_on_signup_button(context):
    context.google_page.fill_details_and_sign_up()