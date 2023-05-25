from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="/home/hamza/seleniumproject/chromedriver")
    context.driver.maximize_window()
    # context.driver.minimize_window()


@when(u'I Open Login Page')
def step_impl(context):
    test_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_freight&section"
    context.driver.get(test_url)


@then(u'Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.CLASS_NAME, "input").send_keys(user)
    context.driver.find_element(By.ID, "user_pass").send_keys(pwd)


@then(u'Click on submit button')
def step_impl(context):
    context.driver.find_element(By.ID, "wp-submit").click()


@then(u'User will be successfully logged in')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div[1]/div[5]/form/ul/li[1]/a").click()
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_small&section"
    url = context.driver.current_url
    if url == expected_url:
        assert True, "Login Successfull"
    else:
        assert False, "Invalid Credentials"


@then(u'User will not be successfully logged in')
def step_impl(context):
    expected_url = "https://wpqa1.eniture-qa.com/wp-admin/admin.php?page=wc-settings&tab=fedex_small&section"
    url = context.driver.current_url
    if url == expected_url:
        assert True, "Login Successfull"
    else:
        assert False, "Invalid Credentials"

