import time
import datetime
from datetime import datetime
from datetime import timedelta

import selenium.webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import unittest

driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hotwire.com/")
bundles_input = driver.find_element(By.CSS_SELECTOR, 'div[data-bdd="farefinder-option-bundles"]').click()

class test_Travel(unittest.TestCase):

    def test_Fly_from(self):
        fly_from = driver.find_element(By.CSS_SELECTOR, 'input[data-bdd = "farefinder-package-origin-location-input"]').send_keys("SFO")
        fly_from = driver.find_element(By.CSS_SELECTOR, 'input[value]').send_keys("San Francisco, CA, United States of America (SFO-San Francisco Intl.)")
        time.sleep(1.0)

    def test_Fly_to(self):
        fly_too = driver.find_element(By.CSS_SELECTOR, 'input[data-bdd = "farefinder-package-destination-location-input"]').send_keys("LAX")
        fly_too = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xs-12 margin-top-4"] input[value]').send_keys("Los Angeles, CA, United States of America (LAX-Los Angeles Intl.)")
        time.sleep(1.0)

    def test_Timpul(self):
        departing = driver.find_element(By.CSS_SELECTOR, '.form-combined__input1>div:nth-child(2)')
        departing.click()
        dep_date = driver.find_element(By.CSS_SELECTOR, 'td[aria-label="February 14, 2022"]')
        dep_date.click()
        ret_date = driver.find_element(By.CSS_SELECTOR, 'td[aria-label="February 28, 2022"]')
        ret_date.click()

        #time.sleep(3.0)

    def test_PickUP(self):
        car = driver.find_element(By.CSS_SELECTOR, 'button[data-bdd="farefinder-package-bundleoption-car"]').click()
        select1 = Select(driver.find_element(By.NAME, "carPickupTime"))
        select1.select_by_visible_text('Evening')

        select2 = Select(driver.find_element(By.NAME, "carDropoffTime"))
        select2.select_by_visible_text('Morning')

        time.sleep(2.0)

    def test_clicuri(self):
        # wait = WebDriverWait(driver, 3)
        # element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[class="picker__popover Tooltip Tooltip--bottom Tooltip--popover Tooltip--lg in fade"] .Tooltip__inner .btn.btn-link.picker__clear .btn__label')))

        clic = driver.find_element(By.CSS_SELECTOR, '.col-xs-12.margin-top-4 .guest-picker')
        clic.click()
        time.sleep(1.0)
        d_clic = driver.find_element(By.CSS_SELECTOR, '.row.popover-actions.guest-picker-apply .btn__label')
        d_clic.click()
        time.sleep(1.0)

    def test_new_timeperiod(self):
        depart = driver.find_element(By.CSS_SELECTOR, '.form-combined__input1>div:nth-child(2)')
        depart.click()
        #today = datetime.now()
        next_day = datetime.today() + timedelta(days=1)
        next_day20 = datetime.today() + timedelta(days=20)
        next_day_detailed = next_day.strftime('%B %d, %Y')
        next_day20_detailed = next_day20.strftime('%B %d, %Y')
        print()
        print(next_day_detailed)
        print(next_day20_detailed)

        if next_day_detailed[-8] == "0":
            next_day_detailed = next_day_detailed.replace(next_day_detailed[-8], "", 1)
        print("conversion of next day", next_day_detailed)
        if next_day20_detailed[-8] == "0":
            next_day20_detailed = next_day20_detailed.replace(next_day20_detailed[-8], "", 1)
        print("conversion of 20+ day", next_day20_detailed)

        date_go = 'td[aria-label*=\"' + next_day_detailed + '\"]'
        date_back = 'td[aria-label*=\"' + next_day20_detailed + '\"]'
        dep_date = driver.find_element(By.CSS_SELECTOR, date_go)
        dep_date.click()
        ret_date = driver.find_element(By.CSS_SELECTOR, date_back)
        ret_date.click()

    if __name__ == '__main__':
        unittest.main()
        driver.quit()



