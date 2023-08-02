from selenium.webdriver.common.by import By
def mobile_verify(driver, action):
   actual = True
   expected = False
   try:
      input_element = driver.find_element(By.CSS_SELECTOR,
                                          "input[placeholder='চাকরি প্রার্থীর ১১ সংখ্যার মোবাইল নাম্বার দিন']")
      input_element.send_keys("01715244961")
      element = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue to Apply')]")
      action.click_to_btn_js(driver, element)
      expected = True
   except Exception as e:
      pass
   assert actual == expected