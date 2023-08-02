from selenium.webdriver.common.by import By
def ans_is_yes_for_question(driver, action):
   actual = True
   expected = False
   try:
      element = driver.find_element(By.XPATH, "//button[contains(text(), 'এগিয়ে যান')]")
      action.click_to_btn_js(driver, element)
      buttons = driver.find_elements(By.CSS_SELECTOR,
                                    '.shadow-md.p-4.w-full')
      for button in buttons:
         element = button.find_element(By.XPATH, "//input[@type='radio' and @value='yes']")
         action.click_to_btn_js(driver, element)

      element = driver.find_element(By.XPATH, "//button[contains(text(), 'যোগ্যতা পরীক্ষা')]")
      action.click_to_btn_js(driver, element)
      input_element = driver.find_element(By.CSS_SELECTOR,
                                          "input[placeholder='চাকরি প্রার্থীর ১১ সংখ্যার মোবাইল নাম্বার দিন']")

      expected = True
   except Exception as e:
      pass

   assert actual == expected