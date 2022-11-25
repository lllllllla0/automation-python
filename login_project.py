import pandas as pd
import calculate
from selenium.webdriver.common.keys import Keys
import time
# scrape simple data from selenium
from selenium import webdriver
from datetime import datetime as dt

# additional codes needed to run in pycharm
# from selenium.webdriver.chrome.service import Service
# service = Service('direction/chromedriver.exe')
# driver = webdriver.Chrome(service = service, options = options)


# how to get the temp without log in
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


def clean_text(text):
  output = float(text.split(": ")[1])
  return output


def write_file(text):
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
  with open(filename, 'w') as file:
    file.write(text)


def main():
  driver = get_driver()
  while True:
    time.sleep(2)
    element = driver.find_element(by='xpath',
                                  value="/html/body/div[1]/div/h1[1]")
  #  element = driver.find_element(by='xpath', value="/html/body/div[1]/div/h1[2]")
  text = str(clean_text(element.text))
  write_file(text)


print(main())
