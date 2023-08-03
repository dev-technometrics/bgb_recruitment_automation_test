from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def ans_is_yes_for_question(driver, action):
   actual = True
   expected = False
   try:
      element = driver.find_element(By.XPATH, "//button[contains(text(), 'এগিয়ে যান')]")
      action.click_to_btn_js(driver, element)
      x_path = "input[type='radio'][value='yes']"
      wait = WebDriverWait(driver, 10)
      wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, x_path)))
      yes_radio_buttons = driver.find_elements(By.CSS_SELECTOR, x_path)
      for button in yes_radio_buttons:
         button.click()

      element = driver.find_element(By.XPATH, "//button[contains(text(), 'যোগ্যতা পরীক্ষা')]")
      action.click_to_btn_js(driver, element)
      input_element = driver.find_element(By.CSS_SELECTOR,
                                          "input[placeholder='চাকরি প্রার্থীর ১১ সংখ্যার মোবাইল নাম্বার দিন']")

      expected = True
   except Exception as e:
      pass

   assert actual == expected