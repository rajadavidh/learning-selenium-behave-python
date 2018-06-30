from behave import *
from selenium import webdriver


@given("I am hungry")
def step_impl(context):
    pass


@when("my mother is shopping")
def step_impl(context):
    url = 'http://www.seleniumframework.com'
    context.browser.get(url)


@then("I cook a meal")
def step_impl(context):
    print ("print debug #1")
    print ("print debug #2")
    print ("print debug #3")  # this line is not printed
