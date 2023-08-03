import argparse
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def send_value_to_palceholder(driver, text, value):
   css =  f"input[placeholder='{text}']"
   wait = WebDriverWait(driver, 10)
   wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, css)))
   input_element = driver.find_element(By.CSS_SELECTOR,css)
   input_element.send_keys(value)

def click_to_button_as_text(driver, text):
    login_xpath = f"//button[contains(text(), '{text}')]"
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, login_xpath)))
    element = driver.find_element(By.XPATH, login_xpath)
    element.click()
    time.sleep(3)

def load_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_page',
                        help='start page',
                        default=1)
    parser.add_argument('--end_page',
                        help='end page',
                        default=489)
    parser.add_argument('--book_url',
                        help='book_url',
                        default='https://bdebooks.com/books/1001-motivational-quotes-for-success-by-thomas-j-vilord-by-bdebooks/')
    args = parser.parse_args()
    args.start_page = int(args.start_page)
    args.end_page = int(args.end_page)
    return args

def make_dir_if_not_exists(file_path):
    dirs = file_path.split('/')
    if dirs:
        path = ''
        for dir in dirs:
            if dir:
                path = path + dir + '/'
                if not os.path.exists(path):
                    os.mkdir(path)