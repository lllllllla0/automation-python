# this is a test
import pandas as pd
import calculate
from selenium.webdriver.common.keys import Keys
import time

print('hello world')

x = 10
y = x * 2
z = y + 20
print(z)

# scrape simple data from selenium
from selenium import webdriver

# additional codes needed to run in pycharm
# from selenium.webdriver.chrome.service import Service
# service = Service('direction/chromedriver.exe')
# driver = webdriver.Chrome(service = service, options = options)


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


def clean_test(text):
  output = float(text.split(': ')[1])
  return output


def main():
  driver = get_driver()
  element = driver.find_element(by='xpath',
                                value="/html/body/div[1]/div/h1[1]")
  #  element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")
  return clean_test(element.text)


#print(main())

# baidu = webdriver.Chrome()
# baidu.get('https://www.baidu.com')


# how to login with selenium
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
  driver.get('http://automated.pythonanywhere.com/login/')
  return driver


def main():
  driver = get_driver()
  driver.find_element(by='id', value="id_username").send_keys('automated')
  driver.find_element(
    by='id', value="id_password").send_keys('automatedautomated' + Keys.RETURN)
  #  element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")
  print(driver.current_url)
  #return element.text


print(main())

#
