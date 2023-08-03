import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.common import send_value_to_palceholder, click_to_button_as_text


def pay(driver):
   actual = True
   expected = False
   try:
      login_xpath = "//button[contains(text(), 'Pay Now')][last()]"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.XPATH, login_xpath)))
      element = driver.find_element(By.XPATH, login_xpath)
      element.click()
      time.sleep(3)

      click_to_button_as_text(driver, 'PAY NOW')
      send_value_to_palceholder(driver, 'Card Number', '4111111111111111')
      send_value_to_palceholder(driver, 'MM/YY', '12/28')
      send_value_to_palceholder(driver,  'CVV/CVC', '100')
      send_value_to_palceholder(driver, 'Card Holder Name', 'test')
      click_to_button_as_text(driver, 'PAY NOW')

      login_xpath =  "//input[@name='submit']"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.XPATH, login_xpath)))
      element = driver.find_element(By.XPATH, login_xpath)
      element.click()
      time.sleep(3)

      expected = True
   except Exception as e:
      pass
   assert actual == expected