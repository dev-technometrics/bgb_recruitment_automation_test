from selenium.webdriver.common.by import By
def goto_eligiblecheck_page(driver, action):
   btn_css = '.rounded-full.bg-\[\#00B074\]'
   download_btn = driver.find_element(By.CSS_SELECTOR, f'{btn_css}')
   action.click_to_btn_js(driver, download_btn)
   current_url = driver.current_url
   actual = True
   expected = False
   if 'eligiblecheck' in current_url:
      expected = True
   assert actual == expected