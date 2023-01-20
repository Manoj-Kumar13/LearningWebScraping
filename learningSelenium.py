from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

os.environ['PATH'] += r"C:\seleniumDrivers"
# to prevent browser closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

website_url = "https://www.selenium.dev/selenium/web/web-form.html"
# driver.get(website_url)
# title = driver.title
# print(title)

# finding an element
# text_box = driver.find_element(by=By.NAME, value="my-text")
# pass_box = driver.find_element(by=By.NAME, value="my-password")
# textarea_box = driver.find_element(by=By.NAME, value="my-textarea")
# check_box = driver.find_element(by=By.NAME, value="my-check")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
#
# # taking actions
# text_box.send_keys("Selenium")
# pass_box.send_keys("selenium strong pass")
# textarea_box.send_keys("this is the text selenium gonna receive")
# check_box.click()
# submit_button.click()
#
# message = driver.find_element(by=By.ID, value="message")
# WebDriverWait(driver,3).until(
#     ec.text_to_be_present_in_element((By.ID, 'message'), "Received!")
# )

website_url="https://booking.com"
driver.get(website_url)
title = driver.title
print(title)

currency_button = driver.find_element(
            By.XPATH,'/html/body/header/nav[1]/div[2]/div[1]/button'
        )
currency_button.click()
driver.implicitly_wait(10)

select_currency = driver.find_element(
            By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency=INR"]'
        )
select_currency.click()

# time.sleep(5)
# driver.quit()