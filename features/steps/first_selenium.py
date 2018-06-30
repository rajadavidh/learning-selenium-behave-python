from behave import *
from selenium import webdriver
chrome_driver_path = "/Users/rajadavid/PycharmProjects/learning-selenium-behave-python/chromedriver"


@given("I open selenium framework website")
def step_impl(context):
    context.driver = webdriver.Chrome(chrome_driver_path)
    url = 'http://www.seleniumframework.com'
    context.driver.get(url)


@then("I print the title")
def step_impl(context):
    # context.driver.implicitly_wait(10)
    # title = context.driver.title

    # Untuk lihat hasilnya, tambahkan --no-capture waktu run commandline
    # Contoh: behave --no-capture --no-capture-stderr first_selenium.feature
    # print (title)
    print ("print debug #1")
    print ("print debug #2")
    print ("print debug #3")  # this line is not printed

    # Print screenshot
    context.driver.save_screenshot("_failed.png")

    # try:
    #     context.driver.set_script_timeout(5)
    #     context.driver.execute_script("return jQuery.active")
    # except(Exception):
    #     traceback.print_exc()

    # Print screenshot - initial
    # print('scenario status' + scenario.status)
    # if scenario.status == 'failed':
    #     context.driver.save_screenshot(scenario.name + "_failed.png")
    # context.driver.quit()
