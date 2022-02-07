import time
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.chrome import ChromeDriver
from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionsChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(chrome_options=chrome_options)

# options = webdriver.ChromeOptions()
# d = webdriver.DesiredCapabilities.CHROME
# d["loggingPrefs"] = {"browser": "ALL"}
# driver = webdriver.Chrome(options=options, desired_capabilities=d)
# driver.implicitly_wait(5)

driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hotwire.com/")
bundles_input = driver.find_element(By.CSS_SELECTOR, 'div[data-bdd="farefinder-option-bundles"]').click()
class Travel:
    def Fly_from():
        fly_from = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xs-12 margin-top-6"] div[class="location-typeahead"]>label[class="heading-300"]')
        f = fly_from.text
        assert f == "Fly from", "Ok"
        fly_from = driver.find_element(By.CSS_SELECTOR, 'input[data-bdd = "farefinder-package-origin-location-input"]').send_keys("SFO")
        fly_from = driver.find_element(By.CSS_SELECTOR, 'input[value]').send_keys("San Francisco, CA, United States of America (SFO-San Francisco Intl.)")
        time.sleep(1.0)

    def Fly_to():
        fly_too = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xs-12 margin-top-4"] div[class="location-typeahead"]>label[class="heading-300"]')
        ff = fly_too.text
        assert ff == "Fly to", "Ok"
        fly_too = driver.find_element(By.CSS_SELECTOR, 'input[data-bdd = "farefinder-package-destination-location-input"]').send_keys("LAX")
        fly_too = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xs-12 margin-top-4"] input[value]').send_keys("Los Angeles, CA, United States of America (LAX-Los Angeles Intl.)")
        time.sleep(1.0)

r1 = Travel
r1.Fly_from()
r2 = Travel
r2.Fly_to()

dep = driver.find_element(By.CSS_SELECTOR, 'div.form-combined__input1 > div.form-group input[name="startDate"]')
dep = driver.find_element(By.CSS_SELECTOR, 'div.form-combined__input1 input[name="startDate"]').send_keys("02/08/2022")

ret3 = driver.find_element(By.CSS_SELECTOR, 'input[data-wdio="farefinder-package-date-range-input-end"]').send_keys("02/27/2022")       #    DA

car = driver.find_element(By.CSS_SELECTOR, 'button[data-bdd="farefinder-package-bundleoption-car"]').click()
select1 = Select(driver.find_element(By.NAME, "carPickupTime"))
select1.select_by_visible_text('Evening')

select2 = Select(driver.find_element(By.NAME, "carDropoffTime"))
select2.select_by_visible_text('Morning')

time.sleep(3.0)

deal = driver.find_element(By.CSS_SELECTOR, 'button[data-bdd="farefinder-package-search-button"]')
deal.click()
#time.sleep(1,0)
# deal = driver.get("https://vacation.hotwire.com/Hotel-Search?adults=2&airlineCode&cabinClass=COACH&destination=Los%20Angeles%20%28and%20vicinity%29%2C%20California%2C%20United%20States%20of%20America&directFlights=false&dropOffTime=1030&endDate=2022-02-08&infantsInSeats=0&mdpcid=50572-30031.5707879897&misId=AgitmuXO5Zjd_hIQyrqqxai-2-KTASD-19wu~ARIIGgIIAiDo8AoaMggBEhYKA1NGTxjTjL0CKgoyMDIyLTAyLTA3EhYKA0xBWBjMguECKgoyMDIyLTAyLTA4IgA&origin=San%20Francisco%2C%20CA%2C%20United%20States%20of%20America%20%28SFO-San%20Francisco%20Intl.%29&paandi=true&packageType=fhc&partialStay=false&pickUpTime=1030&regionId=178280&searchProduct=hotel&semdtl=&sort=RECOMMENDED&startDate=2022-02-07&theme=&tmid=32213609859&tripType=ROUND_TRIP&useRewards=false&userIntent=")
# search = driver.find_element(By.CSS_SELECTOR, 'div.uitk-cell > button[datastid="submit-hotel-search"]')
# search.click()
# time.sleep(4.0)
# driver.close()

drivere = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
drivere.get("https://vacation.hotwire.com/Hotel-Search?adults=2&airlineCode&cabinClass=COACH&destination=Los%20Angeles%20%28and%20vicinity%29%2C%20California%2C%20United%20States%20of%20America&directFlights=false&dropOffTime=1030&endDate=2022-02-08&infantsInSeats=0&mdpcid=50572-30031.5707879897&misId=AgitmuXO5Zjd_hIQyrqqxai-2-KTASD-19wu~ARIIGgIIAiDo8AoaMggBEhYKA1NGTxjTjL0CKgoyMDIyLTAyLTA3EhYKA0xBWBjMguECKgoyMDIyLTAyLTA4IgA&origin=San%20Francisco%2C%20CA%2C%20United%20States%20of%20America%20%28SFO-San%20Francisco%20Intl.%29&paandi=true&packageType=fhc&partialStay=false&pickUpTime=1030&regionId=178280&searchProduct=hotel&semdtl=&sort=RECOMMENDED&startDate=2022-02-07&theme=&tmid=32213609859&tripType=ROUND_TRIP&useRewards=false&userIntent=")
searcher = drivere.find_element(By.CSS_SELECTOR, 'button[class="uitk-button uitk-button-large uitk-button-fullWidth uitk-button-has-text uitk-button-primary"]').click()
time.sleep(3.0)

driver.quit()


