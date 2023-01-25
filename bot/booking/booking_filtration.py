from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exp

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, star_values):
        pass

    def sort_lowest_price_first(self):
        try:
            sorting_ele = WebDriverWait(self.driver, 10). \
                until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')))
            sorting_ele.click()
        except exp.TimeoutException:
            sorting_ele = WebDriverWait(self.driver,10).\
                until(EC.element_to_be_clickable(
                (By.XPATH, '/html/body/div[22]/div/div/div/div/ul/li[3]/button')))
            sorting_ele.click()
        except:
            print("general error occurred")
