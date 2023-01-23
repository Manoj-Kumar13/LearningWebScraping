import time
import bot.booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exp

class Booking(webdriver.Chrome):
    # to stop chrome from closing automatically
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    def __init__(self,driver_path="C:\seleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__(options=Booking.options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self,currency=None):
        try:
            currency_button = WebDriverWait(self,1).\
                until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[data-tooltip-text="Choose your currency"]')))
        except:
            print("inside except choosing currency btn")
            currency_button =WebDriverWait(self, 1). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')))

        currency_button.click()

        try:
            select_currency = WebDriverWait(self, 1). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')))
        except:
            print("inside except choosing currency")
            select_currency = WebDriverWait(self, 1). \
                until(EC.element_to_be_clickable(
                (By.XPATH, f'//div[text()="{currency}"]')))

        # print(select_currency)
        select_currency.click()

    def select_place_to_go(self,place_to_go:str):

        try:
            input_ele = self.find_element(By.CSS_SELECTOR,'input[placeholder="Where are you going?"]')
            input_ele.clear()
            input_ele.send_keys(place_to_go)
        except:
            print("input element not found")

        # finding first place in suggested list
        try:
            # self.implicitly_wait(5)
            first_result = self.find_element(
                By.CSS_SELECTOR,'li[data-i="0"]'
            )
        except:
            print("inside except first result")
            first_result = self.find_element(By.CSS_SELECTOR, 'li[class="a80e7dc237"]')
            # print("suggestions not found")
        first_result.click()

    def select_dates(self,check_in_date:str, check_out_date:str):

        try:
            check_in_ele = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
        except:
            print("inside except check in date")
            check_in_ele = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')

        check_in_ele.click()

        try:
            check_out_ele = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
        except:
            print("inside except check out date")
            check_out_ele = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')

        check_out_ele.click()

    def select_adults(self,adults:int):
        try:
            input_ele = self.find_element(By.CSS_SELECTOR,'label[id="xp__guests__toggle"]')
        except:
            print("inside except adults input element")
            input_ele = self.find_element(By.CSS_SELECTOR, 'div[class="d67edddcf0"]')

        input_ele.click()

        try:
            decrease_btn = self.find_element(
                By.XPATH ,
                '/html/body/div[1]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]'
            )

        except exp.NoSuchElementException:
            decrease_btn=self.find_element( By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
        except:
            decrease_btn = self.find_element(
                By.XPATH,
                '/html/body/div[2]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]'
            )
        decrease_btn.click()

        # try:
        submit_btn = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        # except:
        #     print("submit btn not found")
        submit_btn.click()


