import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def send_otp(driver, action):
   actual = True
   expected = False
   try:
      input_element = driver.find_element(By.CSS_SELECTOR,
                                          "input[placeholder='চাকরি প্রার্থীর ১১ সংখ্যার মোবাইল নাম্বার দিন']")
      mob_no = input("Enter your mobile number : ")
      # mob_no = '01715244961'
      input_element.send_keys(mob_no)
      element = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue to Apply')]")
      action.click_to_btn_js(driver, element)
      expected = True
   except Exception as e:
      pass
   assert actual == expected

def mobile_verify_login(driver, action):
   actual = True
   expected = False
   try:
      input_element = driver.find_element(By.CSS_SELECTOR,
                                          'input[type="text"]')
      otp = input("Enter the OTP : ")
      # otp = '123'
      input_element.send_keys(f'{otp}')
      time.sleep(3)
      element = driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]")
      element.click()
      time.sleep(3)

      id_pass_css = "input[type='text']"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, id_pass_css)))
      input_elements = [e.get_attribute("value") for e in driver.find_elements(By.CSS_SELECTOR, id_pass_css)]
      id = input_elements[0]
      password = input_elements[1]
      element = driver.find_element(By.XPATH, "//a[contains(text(), 'Go to Login')]")
      element.click()
      time.sleep(3)

      login_css = "input[placeholder='ইউজার আইডি']"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, login_css)))
      input_element = driver.find_element(By.CSS_SELECTOR,login_css)
      input_element.send_keys(id)

      login_css = "input[placeholder='পাসওয়ার্ড']"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, login_css)))
      input_element = driver.find_element(By.CSS_SELECTOR, login_css)
      input_element.send_keys(password)

      login_xpath =  "//button[contains(text(), 'Login')]"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.XPATH, login_xpath)))
      element = driver.find_element(By.XPATH,login_xpath)
      element.click()
      time.sleep(3)

      body = driver.find_element(By.CSS_SELECTOR,'body').text
      if 'ফি প্রদান করুন' in body:
         expected = True
   except Exception as e:
      pass
   assert actual == expected