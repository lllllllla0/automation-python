# this is a test
import pandas as pd
import calculate

print('hello world')

x = 10
y = x * 2
z = y + 20
print(z)

# scrape simple data from selenium
from selenium import webdriver


def get_driver():
  # set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument('disable-infobars')  #disable infor board
  options.add_argument(
    'start-maximized')  #start the browser at the maximized version
  options.add_argument(
    'disable-dev-shm-usage')  # avoid issues with dev+shm+usage
  options.add_argument('no-sandbox')  #
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')
  driver = webdriver.Chrome(options=options)
  driver.get('http://automated.pythonanywhere.com')
  return driver


def main():
  driver = get_driver()
  element = driver.find_element(by='xpath',
                                value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
