from behave import *
#from selenium import webdriver
#chrome_driver_path = "/Users/rajadavid/PycharmProjects/test_framework/chromedriver"

# @given('I open chrome browser')
# def step_impl(context):
#    context.driver = webdriver.Chrome(chrome_driver_path)
#    url = 'http://www.seleniumframework.com'
#    context.driver.get(url)
#    driver.quit()

# @given('I open chrome browser')
# def step_impl(context):
#    context.driver = webdriver.Chrome(chrome_driver_path)
#    #driver.quit()


# @given('I open selenium framework website')
# def step_impl(context):
#    context.chrome_path = "/Users/rajadavid/PycharmProjects/test_framework/chromedriver"
#    driver = webdriver.Chrome(context.chrome_path)
#    url = 'http://www.seleniumframework.com'
#    driver.get(url)
#    title = driver.title
#    assert "Selenium" in title

#@given('I open selenium framework website')
def step_impl(context):
   #pass
   context.a = 1
   context.b = 2
   # context.chrome_path = "/Users/rajadavid/PycharmProjects/test_framework/chromedriver"
   # driver = webdriver.Chrome(context.chrome_path)
   # url = 'http://www.seleniumframework.com'
   # driver.get(url)
#@when('I open web')
def step_impl(context):
  driver = webdriver.Chrome('/Users/rajadavid/PycharmProjects/learning-selenium-behave-python/chromedriver')
  driver.get('http://www.google.com')
  context.sum = int(context.a) + int(context.b)
#@then('I print the title')
def step_impl(context):
   # pass
   print("Sum of", context.a, "and", context.b, "is:", context.sum)
   # context.driver.get("http://www.seleniumframework.com")
   # #title = context.driver.title
   # print(context.driver.title)
   # #assert "Selenium" in title
   # context.driver.quit()


# driver = webdriver.Chrome(chrome_driver_path)
# url = 'http://www.seleniumframework.com'
# driver.get(url)
# title = driver.title
# assert "Selenium" in title