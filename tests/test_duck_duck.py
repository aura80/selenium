import time
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_check_search():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://duckduckgo.com/")
    add_element_button = driver.find_element(By.CSS_SELECTOR, "form.search--home")      # exercitiu
    add_element = driver.find_element(By.CSS_SELECTOR, "form#search_form_homepage input#search_form_input_homepage")

    search_input = driver.find_element(By.CSS_SELECTOR, "form#search_form_homepage input#search_form_input_homepage")
    search_input.send_keys("python")

    search_button = driver.find_element(By.CSS_SELECTOR, "input#search_button_homepage")
    search_button.click()

    time.sleep(7.0)

#python (search_input.type("python"))
#test_check_search()

def test_check_search1():
    #img[scrset="https://dynamic-media-cdn.tripadvisor.com/media/ph…9/29/d4/jardines-de-luxemburgo.jpg?w=900&h=-1&s=1"]
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/c9/29/d4/jardines-de-luxemburgo.jpg?w=800&h=-1&s=1 1x")
    time.sleep(7.0)
#test_check_search1()

