import pytest
import time
from app_configs.constants import DELAY_LONG
from automation.common.action_element import ActionPerformer
from automation.common.scraping_driver import ScrapingDriver
from automation.elegiblecheck.check import ans_is_yes_for_question
from automation.home.apply_to_job import goto_eligiblecheck_page
from automation.payment.pay import pay
from automation.mobileverification.verify import send_otp, mobile_verify_login
from utils.error_handling import ErrorLogger

MAIN_SITE = 'https://joinborderguard.technometrics.net/'
scraping_driver = ScrapingDriver()
scraping_driver.download_driver()
driver = scraping_driver.execute_driver()
driver.get(f'{MAIN_SITE}')
driver.maximize_window()
time.sleep(DELAY_LONG)
this_filename = '_'.join(__file__.split('/')[-2:])[:-3]
error_logger = ErrorLogger(this_filename)
action = ActionPerformer(error_logger)

def test__when_click_to_appy__should__go_elegiblecheck_page():
   goto_eligiblecheck_page(driver, action)

def test__when_ans_is_yes_for_question__ask_for_phone_and_email():
   ans_is_yes_for_question(driver, action)

def test__when_give_phone_email__should__ask_for_otp():
   send_otp(driver, action)

def test__when_give_otp__should__login():
   mobile_verify_login(driver, action)

def test__when_loggedin__should_pay():
   pay(driver)
